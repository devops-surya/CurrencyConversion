---

# 📦 Currency Conversion Microservice 🚀

A FastAPI-based **Currency Conversion Microservice**, containerized using **Docker**, deployed on **AWS EKS (us-east-1)** using **Helm**, with infrastructure provisioned via **Terraform**, CI pipeline using **GitHub Actions**, and a **Jenkins CI pipeline with an example of Jenkins Shared Library (for visibility placed inside the same repo)**.

---

## ✅ Table of Contents

1. Microservice Manual Deployment (Local Python)
2. Dockerfile and Docker Build
3. CI/CD using GitHub Actions
4. Helm Chart Information
5. Infrastructure Deployment with Terraform + Helm
6. Jenkinsfile Overview (Jenkins CI Pipeline)

   * 6.1 Jenkins Shared Library Example 

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
├── .pre-commit-config.yaml       # Pre-commit hooks for code quality
└── README.md
```

---

### 📌 Pre-commit Hook Setup:

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

Set your API key inside `app/main.py`:

```python
API_KEY = "<YOUR_API_KEY>"
```

Run:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Access:

✅ If running on AWS EC2 or any cloud server:

```
http://<Your-Public-IP>:8000/
```

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

### 📌 Run Docker Container:

```bash
docker run -d -p 8000:8000 currency-converter-app
```

Access:

```
http://<Your-Public-IP>:8000/
```

(For AWS server or any cloud deployment)

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

1. Checkout Code
2. Build Docker Image
3. Run Trivy Image Scan
4. Push to Docker Hub (only if Trivy passes)

---

### 📌 Trigger CI Workflow:

GitHub → Actions → Docker CI Build and Push → Run Workflow → Select Branch → Run

---

## ✅ 4. Helm Chart Information

This project includes a **Helm Chart** for Kubernetes deployment.

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

### 📌 Notes:

* Deployment Type: **NodePort**
* Cluster: **AWS EKS (us-east-1)**
* Helm Chart Path: `helm/currency-converter/`

---

## ✅ 5. Infrastructure Deployment with Terraform + Helm

### 📌 Prerequisites:

| Requirement              | Purpose                                            |
| ------------------------ | -------------------------------------------------- |
| AWS Account              | Deploy infrastructure                              |
| AWS CLI                  | Terraform AWS authentication                       |
| Terraform                | Infrastructure provisioning                        |
| kubectl                  | Interact with EKS                                  |
| Helm                     | Deploy app                                         |
| EC2 Key Pair             | For EKS Node Group SSH access (Name: **EKS-NODE**) |
| (Optional) S3 + DynamoDB | Remote Terraform state                             |

---

### 📌 AWS Region:

* **us-east-1**

---

### 📌 Important Note About EC2 Key Pair:

✅ Make sure you already have an existing EC2 key pair named **`EKS-NODE`**, and that the corresponding `.pem` file is available locally.

This key pair will be used by the EKS node group during Terraform provisioning.

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

✅ Step 1: Configure AWS CLI:

```bash
aws configure
```

✅ Step 2: Initialize Terraform:

```bash
cd terraform
terraform init
```

✅ Step 3: Validate Terraform:

```bash
terraform validate
```

✅ Step 4: Apply Terraform:

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

✅ Step 5: Download kubeconfig (us-east-1):

```bash
aws eks update-kubeconfig --region us-east-1 --name <your-eks-cluster-name>
```

Example:

```bash
aws eks update-kubeconfig --region us-east-1 --name prod-eks-cluster
```

✅ Step 6: Validate EKS Cluster Access:

```bash
kubectl get nodes
kubectl get pods --all-namespaces
```

✅ Step 7: Access NodePort Service:

```bash
kubectl get svc currency-converter
```

Then open in browser:

```
http://<EC2_NODE_PUBLIC_IP>:<NodePort>/
```

✅ Step 8: (Optional) Remote State Backend Example:

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

## ✅ 6. Jenkinsfile Overview (Jenkins CI Pipeline)

### 📌 Folder Structure:

```
CurrencyConversion/
├── Jenkinsfile
├── vars/
│   └── buildAndPush.groovy
└── Jenkinsfile_sharedlibrary
```

---

### 📌 Jenkins Pipeline Stages (Jenkinsfile):

| Stage            | Purpose                                             |
| ---------------- | --------------------------------------------------- |
| Checkout         | Clone Git repository                                |
| Docker Build     | Build Docker image                                  |
| Trivy Image Scan | Scan Docker image for Critical/High vulnerabilities |
| Docker Push      | Push image to Docker Hub                            |
| Health Check     | Test container (curl check)                         |
| Cleanup          | Stop container and clean Docker images/containers   |

---

### 📌 How to Use the Jenkinsfile:

* Create a **Jenkins Pipeline job**.
* Point the job to this Git repository.
* Use the provided `Jenkinsfile` from project root.
* Jenkins agent should have:

  * Docker installed
  * Trivy installed
  * Docker Hub credentials configured (`dockercreds`)

---

### ✅ 6.1 Jenkins Shared Library Example 

For visibility and demo purposes, the **shared library code and its calling Jenkinsfile_sharedlibrary** are included inside the repository.

---

### 📌 Shared Library Folder Structure:

```
CurrencyConversion/
├── vars/
│   └── buildAndPush.groovy     # Reusable shared library logic
└── Jenkinsfile_sharedlibrary   # Pipeline using shared library
```

---

### 📌 Jenkins Setup for Shared Library:

You **must configure the Shared Library** in **Jenkins Global Configuration** before using `Jenkinsfile_sharedlibrary`.

#### Steps to Configure in Jenkins:

1. Go to:
   **Manage Jenkins → Configure System → Global Pipeline Libraries**

2. Add a new Shared Library:

| Field                  | Value                                           |
| ---------------------- | ----------------------------------------------- |
| Library Name           | Example: `jenkins-shared-lib`                   |
| Default Version        | Example: `main`                                 |
| Retrieval Method       | Modern SCM                                      |
| SCM                    | Git                                             |
| Project Repository URL | (Point to this repo for demonstration purposes) |

---

### 📌 Jenkinsfile\_sharedlibrary Usage Example:

```groovy
@Library('jenkins-shared-lib') _

pipeline {
    agent any
    stages {
        stage('Build and Push') {
            steps {
                buildAndPush()
            }
        }
    }
}
```

---

## ✅ Summary:

| Section                | Purpose                                       |
| ---------------------- | --------------------------------------------- |
| Local Python Run       | Local FastAPI testing                         |
| Docker Build           | Containerization                              |
| GitHub Actions CI      | Build → Trivy → Push                          |
| Helm                   | Helm deployment definitions                   |
| Terraform + Helm       | Full Infra & App Deployment                   |
| Jenkins CI             | Build → Trivy → Push → Health Check → Cleanup |
| Jenkins Shared Library | Example Shared Library-based pipeline         |

---

## ✅ License:

For **educational/demo purposes only**.

---


