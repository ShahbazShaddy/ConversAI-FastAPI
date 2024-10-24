FROM python:3.9-slim

WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
ENV ENV_PATH=/app/.env
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
# Shahbaz 
