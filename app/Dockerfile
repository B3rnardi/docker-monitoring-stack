FROM python:3.10-slim

WORKDIR /app    

ENV REDIS_HOST=redis

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY main.py .

EXPOSE 8000

CMD ["python", "-u", "main.py"]