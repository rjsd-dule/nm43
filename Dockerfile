FROM python:3.11-slim

# Instalar dependencias necesarias para pandas y otros paquetes
RUN apt-get update && apt-get install -y gcc libffi-dev build-essential

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["flask", "run"]
