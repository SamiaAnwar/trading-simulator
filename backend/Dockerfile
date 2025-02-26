FROM python:3.10-slim-buster

WORKDIR /app-docker

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
