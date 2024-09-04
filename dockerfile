FROM python:3.7.4-slim
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["python", "meny.py"]
