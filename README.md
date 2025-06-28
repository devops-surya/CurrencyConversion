
This project is a simple **Currency Conversion Microservice** built using **FastAPI**, **Jinja2 templates**, and the **exchangerate.host API** (requires API key).

---

## ✅ Features

✅ Web UI form for currency conversion
✅ REST API endpoint for programmatic conversion
✅ Real-time currency conversion using exchangerate.host
✅ Mandatory API Key authentication
✅ Error handling for API failures and user input issues
✅ Docker containerization
✅ GitHub Actions CI for Docker build and push

---

## ✅ Project Structure

```
currencyconversion/
├── app/
│   ├── main.py              # FastAPI main application
│   └── templates/           # HTML templates
│       ├── index.html       # Currency conversion input form
│       └── result.html      # Displays conversion result
├── requirements.txt         # Python package dependencies
├── Dockerfile               # Docker container build file
└── .github/
    └── workflows/
        └── pipeline.yml     # GitHub Actions CI pipeline for Docker build and push
└── README.md                # Project documentation
```

---

## ✅ Prerequisites

* Python 3.8+
* A valid **API key from** [exchangerate.host](https://exchangerate.host/)
* Docker installed (if using Docker)
* GitHub account (for GitHub Actions)

---

## ✅ Running Locally (Without Docker)

Clone the repository:

```bash
git clone <your-repo-url>
cd currencyconversion
```

Create and activate Python virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Set your API key:

Open `app/main.py` and replace:

```python
API_KEY = "<YOUR_API_KEY_HERE>"
```

with your actual API key, for example:

```python
API_KEY = "xxxxxxxx"
```

Run the FastAPI server:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Access the app locally:

* Web UI: [http://localhost:8000/](http://localhost:8000/)
* API: [http://localhost:8000/convert?from\_=USD\&to=EUR\&amount=100](http://localhost:8000/convert?from_=USD&to=EUR&amount=100)

---

## ✅ Running with Docker

Build the Docker image:

```bash
docker build -t currency-converter-app .
```

Run the Docker container:

```bash
docker run -d -p 8000:8000 currency-converter-app
```

Check if container is running:

```bash
docker ps
```

Access via:

* Web UI: [http://localhost:8000/](http://localhost:8000/)
* API: [http://localhost:8000/convert?from\_=USD\&to=EUR\&amount=100](http://localhost:8000/convert?from_=USD&to=EUR&amount=100)

---

## ✅ Running on a Cloud Server (Example: AWS EC2)

If you run this on a cloud server like AWS:

* Ensure **Docker is installed** on the server
* Open port `8000` in your cloud firewall (Security Group for AWS EC2)
* Run the container on the server:

```bash
docker run -d -p 8000:8000 currency-converter-app
```

Access from your browser:

```
http://<your-ec2-public-ip>:8000/
```

---

## ✅ CI Pipeline using GitHub Actions (Only CI – No CD)

We use **GitHub Actions CI pipeline** to:

✅ Build the Docker image
✅ Login to Docker Hub
✅ Push the Docker image to Docker Hub

There is **no CD / deployment step inside the GitHub pipeline**.

---

### 📌 Pipeline File Location:

```
.github/workflows/pipeline.yml
```

---

### 📌 GitHub Secrets Setup (Mandatory Before Pipeline Run):

Go to your repo → **Settings → Secrets → Actions → New repository secret**

Add these two secrets:

| Secret Name         | Example Value                                            |
| ------------------- | -------------------------------------------------------- |
| DOCKERHUB\_USERNAME | Your Docker Hub username                                 |
| DOCKERHUB\_TOKEN    | Your Docker Hub token (from Docker Hub Account Settings) |

---

### 📌 Triggering the CI Pipeline Manually:

1. Go to your GitHub repository → **Actions tab**
2. Find workflow named:
   **"Docker CI Build and Push"**
3. Click: **Run workflow**
4. Select branch (e.g., `main`)
5. Click: **Run workflow**

The job will **checkout code → build Docker → push Docker image to Docker Hub**

---

### 📌 What Happens in CI Pipeline?

| Step                | Purpose                           |
| ------------------- | --------------------------------- |
| Checkout code       | Pulls source from GitHub          |
| Docker buildx setup | Prepares Docker build environment |
| Docker Hub login    | Authenticates to Docker Hub       |
| Docker build        | Builds Docker image               |
| Docker push         | Pushes Docker image to Docker Hub |

---

### 📌 Where Your Docker Image Goes After CI?

Docker Hub Repo:

```
https://hub.docker.com/r/<YOUR_USERNAME>/currencyconversion
```

(For example: `https://hub.docker.com/r/tejamvs/currencyconversion`)

---

## ✅ How the Code Works

| Layer         | File                        | Purpose                                      |
| ------------- | --------------------------- | -------------------------------------------- |
| Web Frontend  | `index.html`                | HTML form for user input                     |
| FastAPI Route | `main.py → "/"`             | Serves the input form                        |
| FastAPI Route | `main.py → "/convert-form"` | Handles form submission and conversion       |
| REST API      | `main.py → "/convert"`      | Converts currency via GET params             |
| External API  | exchangerate.host           | Provides live currency rates (needs API key) |

---

## ✅ Stopping Docker Container (Optional Cleanup)

```bash
docker ps        # Get container ID
docker stop <ID> # Stop container
```

---

## ✅ License

This project is for educational and demonstration purposes only.


