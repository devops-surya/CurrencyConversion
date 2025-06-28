This project is a simple **Currency Conversion Microservice** built using **FastAPI** and **Jinja2 templates**, using the **exchangerate.host API** (requires API key).

It provides both:

* ✅ A **Web UI form** for currency conversion
* ✅ A **REST API endpoint** for programmatic conversion

---

## ✅ Features

* ✅ Real-time currency conversion using [exchangerate.host](https://exchangerate.host/)
* ✅ Mandatory API Key authentication
* ✅ Web UI + REST API Support
* ✅ Simple, clean FastAPI code structure
* ✅ Error handling for API failures and user input issues

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
└── README.md                # Project documentation
```

---

## ✅ Prerequisites

* Python 3.8+
* A valid API key from [exchangerate.host](https://exchangerate.host/)

---

## ✅ Setup Instructions (Run Locally)

Clone the repository or download the source code:

```bash
git clone <your-repo-url>
cd currencyconversion
```

Create a Python virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install required Python packages:

```bash
pip install -r requirements.txt
```

Open `app/main.py` and set your API key:

```python
API_KEY = "<YOUR_API_KEY_HERE>"
```

Example:

```python
API_KEY = "c63ad6ca7000cd4270b5d7e250569d4a"
```

Run the FastAPI application locally:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

---

## ✅ Access the Application

**Web UI (HTML Form):**

```
http://localhost:8000/
```

**REST API Endpoint Example:**

```
http://localhost:8000/convert?from_=USD&to=EUR&amount=100
```

---

## ✅ How the Code Works

| Layer         | File                        | Purpose                                                  |
| ------------- | --------------------------- | -------------------------------------------------------- |
| Web Frontend  | `index.html`                | HTML form for input                                      |
| FastAPI Route | `main.py → "/"`             | Serves the form                                          |
| FastAPI Route | `main.py → "/convert-form"` | Handles POST form submission and conversion              |
| REST API      | `main.py → "/convert"`      | Allows conversion via URL parameters                     |
| External API  | exchangerate.host           | Provides live currency exchange rates (requires API key) |

---

## ✅ Running with Docker

Build the Docker image:

```bash
docker build -t currency-converter-app .
```

Run the container:

```bash
docker run -d -p 8000:8000 currency-converter-app
```

Verify container status:

```bash
docker ps
```

You should see something like:

```
CONTAINER ID   IMAGE                  PORTS                    STATUS
abc123         currency-converter-app   0.0.0.0:8000->8000/tcp   Up
```

Access the application (while running locally):

```
http://localhost:8000/
```

Example REST API:

```
http://localhost:8000/convert?from_=USD&to=EUR&amount=100
```

---

## ✅ Deploying on a Cloud Server (AWS EC2 Example)

Ensure Docker is installed and running on your cloud server.

Open port 8000 in your cloud provider's firewall/security group.

Example Inbound Rule:

| Type       | Protocol | Port Range | Source    |
| ---------- | -------- | ---------- | --------- |
| Custom TCP | TCP      | 8000       | 0.0.0.0/0 |

Run your Docker container on the server:

```bash
docker run -d -p 8000:8000 currency-converter-app
```

Access the app from your browser:

```
http://<your-server-public-ip>:8000/
```

(Replace `<your-server-public-ip>` with your cloud server’s public IP)

---

## ✅ Stopping the Docker Container (Optional Cleanup)

```bash
docker ps  # Get container ID
docker stop <container_id>
```

---

## ✅ License

This project is for educational and demonstration purposes only.

---

