# MLOPs-zoomcamp-capstone

In this project, we will use about 5% of the total dataset [NYC-TAXI-FARE-PREDICTION](https://www.kaggle.com/c/new-york-city-taxi-fare-prediction). Initially we will perform various exploratory data analysis and feature engineering, then we will train 3 different models (LinearRegression, RandomForestRegression and XGBRegressor) with the assistance of tracking server provided by `DagsHub`. At the time of this project, model registry was not available with DagsHub, so only experiment tracking is done.

## Problem Statement
The problem this project is intended to solve is to predict the `fare_amount` for a given ride. Following details about the ride are given as input variables and we need to predict what will be the `fare_amount` while moving from one location to another in New York City.

## Model Deployment
During experiment tracking RMSE in `fare_amount` was around `4` for `XGBOOST.bin`, so we deploy this model as a flask application. The `prediction_service` contains all the files for model deployment. The service can be containerized by building Docker image from available Dockerfile in the directory.

#### Command to build Docker image of the service
`$ docker build -t nyc-taxi-fare-prediction:v1 . `

#### Command to run the service
`$ docker run -it --rm -p 9696:9696 nyc-taxi-fare-prediction:v1 `
