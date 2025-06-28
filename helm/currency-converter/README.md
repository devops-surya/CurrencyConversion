# 📦 Helm Chart - Currency Converter Microservice (NodePort Service)

This Helm chart deploys the **FastAPI-based Currency Converter microservice** on a **Kubernetes Cluster**, exposing it via **NodePort** so it’s reachable externally.

---

## ✅ Chart Structure

currency-converter/
├── Chart.yaml # Chart metadata
├── values.yaml # Configurable values (image name, port, etc.)
└── templates/
├── deployment.yaml # Kubernetes Deployment manifest
└── service.yaml # Kubernetes NodePort Service manifest

yaml
Copy
Edit

---

## ✅ Prerequisites

- A Kubernetes Cluster (Minikube, Kind, AWS EKS, GKE, etc.)
- Helm 3.x installed on your local machine
- Your Docker image **already pushed** to Docker Hub (example: `tejamvs/currencyconversion:latest`)

---

## ✅ How to Deploy the Helm Chart

From your project root directory:

```bash
helm install currency-converter ./helm/currency-converter
✅ Accessing the Service
After deploying:

bash
Copy
Edit
kubectl get svc
Expected output:

pgsql
Copy
Edit
NAME                        TYPE       CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
currency-converter-service  NodePort   10.X.X.X        <none>        8000:30080/TCP   1m
To access the application:

cpp
Copy
Edit
http://<NodeExternalIP>:30080/
✅ Example API call:

arduino
Copy
Edit
http://<NodeExternalIP>:30080/convert?from_=USD&to=EUR&amount=100
Replace <NodeExternalIP> with your cloud server IP (or Minikube node IP)

✅ How NodePort Works (In Simple Terms)
Your FastAPI app listens on port 8000 inside the container

Kubernetes exposes it externally on port 30080 on the node’s IP address

External users can reach the app by calling NodeExternalIP:30080

✅ Uninstall Helm Release (Optional Cleanup)
bash
Copy
Edit
helm uninstall currency-converter
✅ Mandatory Step: API Key inside App
Before building your Docker image, ensure you’ve set your API Key inside app/main.py like this:

python
Copy
Edit
API_KEY = "YOUR_API_KEY"
✅ Notes
This Helm chart only handles Deployment + NodePort Service.
For production-grade deployment, you should add:

Ingress Controller

Resource limits

Liveness/Readiness Probes

Horizontal Pod Autoscaler (HPA)
