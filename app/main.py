"""
Currency Converter Microservice using FastAPI and exchangerate.host API.
Provides both a web form and REST API for currency conversion.
"""

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import requests

app = FastAPI()

# Setup Jinja2 template directory
templates = Jinja2Templates(directory="app/templates")

# ✅ Mandatory API Key (Set your key here)
API_KEY = "--------"  # Replace with your exchangerate.host API key


@app.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    """
    Serve the HTML currency conversion form.
    """
    currencies = ["USD", "EUR", "GBP", "INR", "JPY", "AUD", "CAD", "CHF"]
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "currencies": currencies}
    )


@app.get("/convert", response_class=HTMLResponse)
async def convert_api(from_: str, to: str, amount: float):
    """
    REST API endpoint for currency conversion using query parameters.

    Example:
    /convert?from_=USD&to=EUR&amount=100
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
        response.raise_for_status()
        data = response.json()

        if not data.get("success"):
            error_info = data.get("error", {}).get(
                "info", "API error or missing data"
            )
            return {"error": error_info}

        converted_amount = data.get("result")
        rate = (
            converted_amount / amount
            if amount != 0 and converted_amount is not None
            else None
        )

        return {
            "from": from_,
            "to": to,
            "amount": amount,
            "exchange_rate": rate,
            "converted_amount": converted_amount
        }

    except requests.exceptions.RequestException as req_error:
        return {"error": f"Request error: {str(req_error)}"}
    except ValueError as json_error:
        return {"error": f"JSON decoding error: {str(json_error)}"}


@app.post("/convert-form", response_class=HTMLResponse)
async def convert_form(
    request: Request,
    from_currency: str = Form(...),
    to_currency: str = Form(...),
    amount: float = Form(...)
):
    """
    Handles HTML form submission for currency conversion and renders result page.
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
        response.raise_for_status()
        data = response.json()

        if not data.get("success"):
            error_message = data.get("error", {}).get(
                "info", "API error or missing data"
            )
            return templates.TemplateResponse(
                "result.html",
                {"request": request, "error": error_message}
            )

        converted_amount = data.get("result")
        rate = (
            converted_amount / amount
            if amount != 0 and converted_amount is not None
            else None
        )

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
            "result.html",
            {
                "request": request,
                "error": f"Request error: {str(req_error)}"
            }
        )
    except ValueError as json_error:
        return templates.TemplateResponse(
            "result.html",
            {
                "request": request,
                "error": f"JSON decoding error: {str(json_error)}"
            }
        )
