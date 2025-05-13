FROM python:3.11-slim

# Evita buffering para ver print()s en tiempo real
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y gcc libffi-dev build-essential

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]