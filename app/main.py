"""
Currency Converter Microservice using FastAPI and exchangerate.host API
"""

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import requests

app = FastAPI()

# Setup Jinja2 template directory
templates = Jinja2Templates(directory="app/templates")

# ✅ Mandatory API Key (Set your key here)
API_KEY = "c63ad6ca7000cd4270b5d7e250569d4a"  # Replace with your exchangerate.host API key

@app.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    """
    Serve the currency conversion form page.
    """
    currencies = ["USD", "EUR", "GBP", "INR", "JPY", "AUD", "CAD", "CHF"]
    return templates.TemplateResponse("index.html", {"request": request, "currencies": currencies})

@app.get("/convert", response_class=HTMLResponse)
async def convert_api(from_: str, to: str, amount: float):
    """
    REST API endpoint: Converts currency using query parameters.
    Example: /convert?from_=USD&to=EUR&amount=100
    """
    api_url = "https://api.exchangerate.host/convert"
    params = {
        "from": from_,
        "to": to,
        "amount": amount,
        "access_key": API_KEY
    }

    try:
        response = requests.get(api_url, params=params, timeout=5)
        data = response.json()

        if response.status_code != 200 or not data.get("success"):
            error_info = data.get("error", {}).get("info", "API error or missing data")
            return {"error": error_info}

        converted_amount = data.get("result")
        rate = converted_amount / amount if amount != 0 else None

        return {
            "from": from_,
            "to": to,
            "amount": amount,
            "exchange_rate": rate,
            "converted_amount": converted_amount
        }

    except requests.exceptions.RequestException as req_error:
        return {"error": f"Request error: {str(req_error)}"}
    except Exception as e:
        return {"error": f"Unexpected error: {str(e)}"}

@app.post("/convert-form", response_class=HTMLResponse)
async def convert_form(request: Request, from_currency: str = Form(...),
                       to_currency: str = Form(...), amount: float = Form(...)):
    """
    Handles HTML form submission and shows conversion result.
    """
    api_url = "https://api.exchangerate.host/convert"
    params = {
        "from": from_currency,
        "to": to_currency,
        "amount": amount,
        "access_key": API_KEY
    }

    try:
        response = requests.get(api_url, params=params, timeout=5)
        data = response.json()

        if response.status_code != 200 or not data.get("success"):
            error_message = data.get("error", {}).get("info", "API error or missing data")
            return templates.TemplateResponse(
                "result.html", {"request": request, "error": error_message}
            )

        converted_amount = data.get("result")
        rate = converted_amount / amount if amount != 0 else None

        return templates.TemplateResponse(
            "result.html",
            {
                "request": request,
                "from_currency": from_currency,
                "to_currency": to_currency,
                "amount": amount,
                "converted_amount": converted_amount,
                "rate": rate,
                "error": None
            }
        )

    except requests.exceptions.RequestException as req_error:
        return templates.TemplateResponse(
            "result.html", {"request": request, "error": f"Request error: {str(req_error)}"}
        )
    except Exception as e:
        return templates.TemplateResponse(
            "result.html", {"request": request, "error": f"Unexpected error: {str(e)}"}
        )
x=1
y=2y=2
