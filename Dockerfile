# Dockerfile

FROM python:3.11-alpine

# Create appuser (non-root)
RUN adduser --disabled-password --gecos '' appuser

WORKDIR /app

# Copy dependencies first
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy app source
COPY app/ ./app

EXPOSE 8000

USER appuser

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

