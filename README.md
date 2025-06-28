---

# 📦 Currency Conversion Microservice 🚀

A simple **Currency Conversion Microservice** built using **FastAPI**, **Jinja2 templates**, and the **exchangerate.host API**.

---

## ✅ Features

✅ Web UI for currency conversion
✅ REST API for programmatic access
✅ Real-time conversion using exchangerate.host
✅ API key-based authentication
✅ Error handling for API failures
✅ Docker containerization
✅ CI using GitHub Actions (Only CI, No CD)
✅ Trivy vulnerability scanning for container image

---

## ✅ Folder Structure (with File Descriptions)

```
CurrencyConversion/
├── Dockerfile                        # Docker build file for creating app container
├── README.md                          # This documentation file
├── app/
│   ├── main.py                        # FastAPI application code
│   └── templates/
│       ├── index.html                 # HTML form for input (currency conversion form)
│       └── result.html                # HTML template to display conversion results
├── helm/
│   └── currency-converter/
│       ├── Chart.yaml                 # Helm chart metadata
│       ├── README.md                  # Instructions for Helm deployment
│       ├── templates/
│       │   ├── deployment.yaml        # Kubernetes deployment spec
│       │   └── service.yaml           # Kubernetes service spec
│       └── values.yaml                # Default Helm values
├── requirements.txt                   # Python production dependencies
├── requirements-dev.txt               # Python dev tools (like pylint)
└── .github/
    └── workflows/
        └── pipeline.yml               # GitHub Actions CI pipeline for Docker build and push
```

---

## ✅ Prerequisites

* Python 3.8+
* Docker installed
* API key from [exchangerate.host](https://exchangerate.host/)
* Trivy installed (for scanning Docker images)
* GitHub account for CI
* **(For AWS EC2)**: Public IP of the EC2 instance and **Port 8000 opened in Security Group**

---

## ✅ Running Locally (Without Docker)

### 1. Clone the repo:

```bash
git clone <your-repo-url>
cd CurrencyConversion
```

### 2. Create Python virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies:

```bash
pip install -r requirements.txt
```

### 4. Set your API key:

Edit `app/main.py`:

```python
API_KEY = "<YOUR_API_KEY>"
```

### 5. Run FastAPI server:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 6. Access locally:

* Web UI: [http://localhost:8000/](http://localhost:8000/)
* API: [http://localhost:8000/convert?from\_=USD\&to=EUR\&amount=100](http://localhost:8000/convert?from_=USD&to=EUR&amount=100)

---

## ✅ Running on AWS EC2 (Cloud Server)

> **Steps for deploying and accessing on AWS EC2:**

### 1. SSH into EC2:

```bash
ssh ec2-user@<your-ec2-public-ip>
```

### 2. Install Docker on Ubuntu (using APT):

```bash
# Update existing packages
sudo apt update
sudo apt install -y apt-transport-https ca-certificates curl software-properties-common gnupg lsb-release

# Add Docker GPG key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# Add Docker repository
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] \
  https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install Docker
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io

# Allow your user to run docker (optional)
sudo usermod -aG docker ubuntu
```

> 🔔 **Logout and login again** for the group change to take effect.

---

Log out and log back in for Docker group changes to take effect.

---

### 3. Open Port 8000 in AWS Security Group:

* Go to AWS EC2 Console → **Your EC2 Instance → Security → Security Groups**
* Edit **Inbound Rules**
* **Add Rule:**
  Type: Custom TCP
  Port: `8000`
  Source: Anywhere (0.0.0.0/0) or Your IP

---

### 4. Build Docker Image **(Important: Run from folder where Dockerfile exists):**

```bash
cd ~/CurrencyConversion  # Or wherever you cloned the project
docker build -t currency-converter-app .
```

---

### 5. Run Docker Container:

```bash
docker run -d -p 8000:8000 currency-converter-app
```

---

### 6. Access from your browser:

```
http://<your-ec2-public-ip>:8000/
```

Example:

```
http://3.110.XXX.XXX:8000/
```

> Replace with your actual EC2 Public IP.

You can access both:

* Web UI: `http://<public-ip>:8000/`
* API: `http://<public-ip>:8000/convert?from_=USD&to=INR&amount=100`

---

## ✅ Docker Image Security Scan with Trivy 🛡️

### 1. Install Trivy:

On EC2:

```bash
curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | sudo sh -s -- -b /usr/local/bin
```

---

### 2. Scan Image (Critical & High Only):

```bash
trivy image --severity CRITICAL,HIGH currency-converter-app
```

---

### 3. How to Reduce Trivy Issues:

| Problem Type       | What You Should Do                              |
| ------------------ | ----------------------------------------------- |
| Critical/High CVEs | Use `python:3.12-slim` or `alpine` base         |
| Python CVEs        | Upgrade `pip`, `setuptools`, and dependencies   |
| OS Package CVEs    | Keep `apt` packages minimal and update packages |
| Old Dependencies   | Update your `requirements.txt` versions         |

---

### ✅ Recommended Dockerfile Hardening Example:

```dockerfile
FROM python:3.12-slim

RUN apt-get update && apt-get install -y build-essential gcc

RUN pip install --no-cache-dir --upgrade pip setuptools wheel

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

After editing, **rebuild and rescan**:

```bash
docker build -t currency-converter-app .
trivy image --severity CRITICAL,HIGH currency-converter-app
```

---

## ✅ CI Pipeline using GitHub Actions

| Stage        | Purpose               |
| ------------ | --------------------- |
| Checkout     | Get code from GitHub  |
| Docker Build | Build container image |
| Docker Push  | Push to Docker Hub    |

---

### GitHub Secrets required:

| Secret Name         | Purpose                  |
| ------------------- | ------------------------ |
| DOCKERHUB\_USERNAME | Your Docker Hub Username |
| DOCKERHUB\_TOKEN    | Docker Hub Token         |

---

### Trigger CI Manually:

1. Go to **GitHub Actions → Docker CI Build and Push**
2. Click **Run Workflow**
3. Select branch → **Run**

---

## ✅ Summary Links:

| Purpose          | Link                                                               |
| ---------------- | ------------------------------------------------------------------ |
| Local UI         | [http://localhost:8000/](http://localhost:8000/)                   |
| AWS EC2 UI       | http\://<ec2-public-ip>:8000/                                      |
| Local API Call   | [http://localhost:8000/convert](http://localhost:8000/convert)?... |
| AWS EC2 API Call | http\://<ec2-public-ip>:8000/convert?                              |

---

## ✅ License:

For  educational/demo use only.

---


