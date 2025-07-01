---

# 📦 Helm Chart - Currency Converter Microservice (NodePort Service)

This Helm chart deploys the **FastAPI-based Currency Converter microservice** on a **Kubernetes Cluster**, exposing it via **NodePort**, making it reachable externally.

---

## ✅ Chart Structure

```
currency-converter/
├── Chart.yaml               # Chart metadata
├── values.yaml              # Configurable values (image name, port, etc.)
└── templates/
    ├── deployment.yaml      # Kubernetes Deployment manifest
    └── service.yaml         # Kubernetes NodePort Service manifest
```

---

## ✅ Prerequisites

* A Kubernetes Cluster (Minikube, Kind, AWS EKS, GKE, etc.)
* Helm 3.x installed on your local machine
* Your Docker image **already pushed** to Docker Hub (e.g., `tejamvs/currencyconversion:latest`)

---

## ✅ How to Deploy the Helm Chart

From your project root directory:

```bash
helm install currency-converter ./helm/currency-converter
```

---

## ✅ Accessing the Service

After deployment, run:

```bash
kubectl get svc
```

You should see an output like:

```
NAME                        TYPE       CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
currency-converter-service  NodePort   10.X.X.X        <none>        8000:30080/TCP   1m
```

### Access the Application:

```
http://<NodeExternalIP>:30080/
```

Where `<NodeExternalIP>` is the public IP of your Kubernetes Node (EC2 public IP if on EKS).

---

## ✅ Example API Call:

```
http://<NodeExternalIP>:30080/convert?from_=USD&to=EUR&amount=100
```

---

## ✅ How NodePort Works (In Simple Terms)

* Your FastAPI app listens on **port 8000 inside the container**
* Kubernetes **exposes the app externally on port 30080 on the Node’s external IP**
* External users can access the service at:
  `http://<NodeExternalIP>:30080/`

---
