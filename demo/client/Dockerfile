FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
EXPOSE 8000
EXPOSE 80/tcp
CMD ["python", "app.py"]
STOPSIGNAL SIGTERM
