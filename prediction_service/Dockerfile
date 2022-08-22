FROM python:3.7.13

RUN pip install -U pip

WORKDIR /app

COPY ["requirements.txt","./"]

RUN pip install -r requirements.txt

COPY ["app.py", "XGBOOST.bin", "./"]

EXPOSE 9696

ENTRYPOINT ["python", "app.py"]

# docker build -t ride-duration-prediction-service:v1 .