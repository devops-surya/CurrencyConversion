from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import requests

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

API_KEY = "c63ad6ca7000cd4270b5d7e250569d4a"

currencies = ["USD", "EUR", "GBP", "INR", "JPY", "AUD", "CAD"]

@app.get("/", response_class=HTMLResponse)
async def show_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "currencies": currencies})

@app.post("/convert-form", response_class=HTMLResponse)
async def handle_form(
    request: Request,
    from_currency: str = Form(...),
    to_currency: str = Form(...),
    amount: float = Form(...)
):
    api_url = "https://api.exchangerate.host/convert"
    params = {
        "from": from_currency,
        "to": to_currency,
        "amount": amount,
        "access_key": API_KEY
    }

    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        data = response.json()

        print("API Response:", data)  # Debugging

        if data.get("success") and data.get("result") is not None and "info" in data and "quote" in data["info"]:
            rate = data["info"]["quote"]
            converted_amount = data["result"]
            result_text = f"{amount} {from_currency} = {converted_amount:.2f} {to_currency} (Rate: {rate})"
        else:
            error_info = data.get("error", {}).get("info", f"API returned unexpected data: {data}")
            result_text = f"API Error: {error_info}"

    except Exception as e:
        result_text = f"Internal Server Error: {str(e)}"

    return templates.TemplateResponse("result.html", {"request": request, "result": result_text})

@app.get("/convert")
def rest_convert(from_: str, to: str, amount: float):
    api_url = "https://api.exchangerate.host/convert"
    params = {
        "from": from_,
        "to": to,
        "amount": amount,
        "access_key": API_KEY
    }

    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        data = response.json()

        print("API REST Response:", data)  # Debugging

        if data.get("success") and data.get("result") is not None and "info" in data and "quote" in data["info"]:
            return {
                "from": from_,
                "to": to,
                "amount": amount,
                "exchange_rate": data["info"]["quote"],
                "converted_amount": data["result"]
            }
        else:
            error_info = data.get("error", {}).get("info", f"API returned unexpected data: {data}")
            return {"error": error_info}

    except Exception as e:
        return {"error": f"Internal Server Error: {str(e)}"}

