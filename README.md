---

# 📦 Currency Conversion Microservice 🚀

A FastAPI-based **Currency Conversion Microservice**, containerized using **Docker**, deployed on **AWS EKS (us-east-1)** using **Helm**, with infrastructure provisioned via **Terraform**, and CI pipeline using **GitHub Actions**.

---

## ✅ Table of Contents

1. [Microservice Manual Deployment (Local Python)](#1-microservice-manual-deployment-local-python)
2. [Dockerfile and Docker Build](#2-dockerfile-and-docker-build)
3. [CI/CD using GitHub Actions](#3-cicd-using-github-actions)
4. [Helm Chart Deployment](#4-helm-chart-deployment)
5. [Infrastructure Deployment with Terraform + Helm](#5-infrastructure-deployment-with-terraform--helm)

---

## ✅ 1. Microservice Manual Deployment (Local Python)

### 📌 Prerequisites:

| Requirement | Purpose                            |
| ----------- | ---------------------------------- |
| Python 3.8+ | Run FastAPI App locally            |
| Virtualenv  | Python environment isolation       |
| API key     | From exchangerate.host API         |
| pre-commit  | Run code quality checks on commits |
| pylint      | Python linting (via pre-commit)    |

---

### 📌 Folder Structure:

```
CurrencyConversion/
├── app/
│   ├── main.py                  # FastAPI app
│   └── templates/
│       ├── index.html           # HTML Input Form
│       └── result.html          # HTML Conversion Result
├── requirements.txt              # Production dependencies
├── requirements-dev.txt          # Development tools (pylint etc.)
├── .pre-commit-config.yaml       # Pre-commit hooks to enforce code quality
└── README.md
```

---

### 📌 Pre-commit Hook:

This project uses **`.pre-commit-config.yaml`** to run **code formatters and pylint checks automatically before every commit**.

**Setup Pre-commit Locally:**

```bash
pip install pre-commit
pre-commit install
```

---

### 📌 Running Locally:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Set API key inside `app/main.py`:

```python
API_KEY = "<YOUR_API_KEY>"
```

Run:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Access:

* Web UI: [http://localhost:8000/](http://localhost:8000/)
* API: [http://localhost:8000/convert?from\_=USD\&to=INR\&amount=100](http://localhost:8000/convert?from_=USD&to=INR&amount=100)

---

## ✅ 2. Dockerfile and Docker Build

### 📌 Prerequisites:

| Requirement | Purpose          |
| ----------- | ---------------- |
| Docker      | Containerization |

---

### 📌 Folder Structure:

```
CurrencyConversion/
├── Dockerfile
├── requirements.txt
├── app/
└── ...
```

---

### 📌 Build Docker Image:

```bash
docker build -t currency-converter-app .
```

---

### 📌 Run Docker Container Locally:

```bash
docker run -d -p 8000:8000 currency-converter-app
```

Access:

```
http://localhost:8000/
```

---

### 📌 Docker Image Security Scan with Trivy:

```bash
curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | sudo sh -s -- -b /usr/local/bin
trivy image --severity CRITICAL,HIGH currency-converter-app
```

---

## ✅ 3. CI/CD using GitHub Actions

### 📌 Prerequisites:

| Requirement        | Purpose                               |
| ------------------ | ------------------------------------- |
| GitHub Account     | CI pipeline                           |
| Docker Hub Account | Push Docker images                    |
| GitHub Secrets     | DOCKERHUB\_USERNAME, DOCKERHUB\_TOKEN |

---

### 📌 Folder Structure:

```
CurrencyConversion/
└── .github/
    └── workflows/
        └── pipeline.yml
```

---

### 📌 CI Pipeline Stages:

| Stage            | Purpose                                         |
| ---------------- | ----------------------------------------------- |
| Checkout         | Pull source code                                |
| Docker Build     | Build Docker image                              |
| Trivy Image Scan | Scan Docker image for Critical/High CVEs        |
| Docker Push      | Push image to Docker Hub (only if Trivy passes) |

---

### 📌 CI Pipeline Flow:

1. **Checkout Code:**
   Pull code from GitHub.

2. **Build Docker Image:**
   Create Docker image tagged as `currency-converter-app`.

3. **Run Trivy Image Scan:**
   Trivy scans for **CRITICAL and HIGH vulnerabilities**.

4. **Push to Docker Hub (only if Trivy scan passes):**
   Image is pushed only if Trivy scan **does not find any Critical/High CVEs**.

---

### 📌 Trigger CI Workflow:

GitHub → Actions → Docker CI Build and Push → Run Workflow → Select Branch → Run

---

## ✅ 4. Helm Chart Deployment

### 📌 Prerequisites:

| Requirement        | Purpose                    |
| ------------------ | -------------------------- |
| Kubernetes Cluster | Deployment target (EKS)    |
| kubectl            | Interact with EKS          |
| Helm               | Kubernetes package manager |

---

### 📌 Folder Structure:

```
CurrencyConversion/
└── helm/
    └── currency-converter/
        ├── Chart.yaml
        ├── values.yaml
        └── templates/
            ├── deployment.yaml
            └── service.yaml
```

---

### 📌 Deployment Notes:

* Deployment Type: **NodePort**
* Cluster: **EKS (us-east-1)**
* Helm Chart Location: **`helm/currency-converter/`**

---

### 📌 Deploy Manually (Optional):

```bash
cd helm/currency-converter
helm install currency-converter .
```

---

### 📌 Access After Helm Deployment:

```bash
kubectl get nodes -o wide
kubectl get svc currency-converter
```

Access app at:

```
http://<EC2_NODE_PUBLIC_IP>:<NodePort>/
```

---

## ✅ 5. Infrastructure Deployment with Terraform + Helm

### 📌 Prerequisites:

| Requirement              | Purpose                       |
| ------------------------ | ----------------------------- |
| AWS Account              | Deploy infrastructure         |
| AWS CLI                  | Terraform AWS authentication  |
| Terraform                | Infrastructure provisioning   |
| kubectl                  | Interact with EKS             |
| Helm                     | Deploy app                    |
| EC2 Key Pair             | For EKS Node Group SSH access |
| (Optional) S3 + DynamoDB | Remote Terraform state        |

---

### 📌 AWS Region:

* **us-east-1**

---

### 📌 Important Note About EC2 Key Pair:

✅ Make sure you already have an **existing EC2 key pair named `EKS-NODE`**, and the corresponding **`.pem` file is available locally**.

This key pair will be used by the EKS node group during provisioning.

---

### 📌 Terraform Folder Structure:

```
CurrencyConversion/
└── terraform/
    ├── backend.tf          # (Optional) S3/DynamoDB backend
    ├── provider.tf         # AWS & Kubernetes providers
    ├── main.tf             # Module orchestration
    ├── variables.tf        # Input variables
    ├── outputs.tf          # Terraform outputs
    └── modules/
        ├── vpc/            # VPC module
        ├── iam/            # IAM module
        ├── eks/            # EKS module
        └── helm/           # Helm deployment module
```

---

### 📌 Deployment Steps:

---

✅ **Step 1: Configure AWS CLI:**

```bash
aws configure
```

---

✅ **Step 2: Initialize Terraform:**

```bash
cd terraform
terraform init
```

---

✅ **Step 3: Validate Terraform:**

```bash
terraform validate
```

---

✅ **Step 4: Apply Terraform:**

```bash
terraform apply
```

Terraform will:

* Create VPC
* Create IAM Roles
* Provision EKS Cluster
* Create Node Group using your EC2 Key Pair
* Setup Kubernetes provider
* Deploy Helm application

---

✅ **Step 5: Download kubeconfig (us-east-1):**

```bash
aws eks update-kubeconfig --region us-east-1 --name <your-eks-cluster-name>
```

Example:

```bash
aws eks update-kubeconfig --region us-east-1 --name prod-eks-cluster
```

---

✅ **Step 6: Validate EKS Cluster Access:**

```bash
kubectl get nodes
kubectl get pods --all-namespaces
```

---

✅ **Step 7: Access NodePort Service:**

```bash
kubectl get svc currency-converter
```

Then open in browser:

```
http://<EC2_NODE_PUBLIC_IP>:<NodePort>/
```

---

✅ **Step 8: (Optional) Remote State Backend:**

Example `backend.tf`:

```hcl
terraform {
  backend "s3" {
    bucket         = "<your-s3-bucket>"
    key            = "currency-converter/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "<your-lock-table>"
  }
}
```

---

## ✅ Summary:

| Section           | Purpose                                 |
| ----------------- | --------------------------------------- |
| Local Python Run  | Local FastAPI testing                   |
| Docker Build      | Containerization                        |
| GitHub Actions CI | Docker Build → Trivy Scan → Docker Push |
| Helm              | Kubernetes deployment spec              |
| Terraform + Helm  | Full Infra and Deployment on AWS        |

---

## ✅ License:

For **educational/demo purposes only**.

---


