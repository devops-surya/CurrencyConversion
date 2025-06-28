Sure Teja! Below is a **professional `README.md`** that:

✅ Assumes **API key is now mandatory**
✅ Shows **exact location in `main.py` where to put your API key**
✅ Removed optional future enhancements section
✅ Focused fully on local running with API key requirement

---

# 📖 Currency Converter Microservice – FastAPI Version (With Mandatory API Key)

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
└── README.md                # Project documentation
```

---

## ✅ Prerequisites

* **Python 3.8+**
* **A valid API key from [exchangerate.host](https://exchangerate.host/)**

---

## ✅ Setup Instructions (Run Locally)

### Step 1: Clone the repository or Download the code

```bash
git clone <your-repo-url>
cd currencyconversion
```

---

### Step 2: Create Python Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### Step 3: Install Required Packages

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install fastapi uvicorn jinja2 requests
```

---

### Step 4: Configure Your API Key in `main.py`

In your **`app/main.py`**, look for this line at the top:

```python
API_KEY = "<YOUR_API_KEY_HERE>"
```

➡️ Replace `<YOUR_API_KEY_HERE>` with your **actual API key** from exchangerate.host.
Example:

```python
API_KEY = "c63ad6ca7000cd4270b5d7e250569d4a"
```

This API key will be used by both the **form-based UI** and the **REST API** to fetch exchange rates.

---

### Step 5: Run the FastAPI Application

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

---

## ✅ Access the Application

### ✅ Web UI (HTML Form):

```
http://localhost:8000/
```

* Fill **From Currency**
* Fill **To Currency**
* Fill **Amount**
* Click Convert

You’ll see the converted amount on the result page.

---

### ✅ REST API Endpoint:

Example call:

```
http://localhost:8000/convert?from_=USD&to=EUR&amount=100
```

Example JSON Response:

```json
{
  "from": "USD",
  "to": "EUR",
  "amount": 100,
  "exchange_rate": 0.85,
  "converted_amount": 85.0
}
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

## ✅ Deployment Notes (For Remote Server)

If running on a cloud server (like AWS EC2):

* ✅ Ensure **port 8000** is open in your firewall/security group.
* ✅ Use `--host 0.0.0.0` to listen on all network interfaces.

Access it via:

```
http://<your-server-public-ip>:8000/
```

---

## ✅ License

This project is for educational and demonstration purposes only.

---

Let me know if you want me to generate your **requirements.txt** or **Dockerfile** next ✅

