FROM python:latest

RUN pip install numpy pandas

WORKDIR /home/app

COPY . .

CMD ["python", "app.py"]