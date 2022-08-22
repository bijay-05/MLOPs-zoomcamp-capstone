# MLOPs-zoomcamp-capstone

In this project, we will use about 5% of the total dataset [NYC-TAXI-FARE-PREDICTION](https://www.kaggle.com/c/new-york-city-taxi-fare-prediction). Initially we will perform various exploratory data analysis and feature engineering, then we will train 3 different models (LinearRegression, RandomForestRegression and XGBRegressor) with the assistance of tracking server provided by `DagsHub`. At the time of working on this project, model registry was not available with DagsHub, so only experiment tracking is done.

## Problem Statement
The problem this project is intended to solve is to predict the `fare_amount` for a given ride. Following details about the ride are given as input variables and we need to predict what will be the `fare_amount` while moving from one location to another in New York City.

Independent Variables (features) = pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude, passenger_count, pickup_datetime

Dependent Variable (target) = fare_amount

## Experiment Tracking
DagsHub provides with tracking server for each repo created. Tracking the experiments with DagsHub was not that difficult as expected, which others can also visualize from a single glance at the notebook cell. Recently, it is announced that now model registry is also available with DagsHub. To view the experiment logs, visit the project repo at [DagsHub](https://dagshub.com/maiden90/mlops-zoomcamp-project)

## Workflow Orchestration
Since this project was not developed on cloud, there is just a basic workflow defining tasks and flow in `model_training_pipeline.py`. This gives observability around the functions in the pipeline. 

## Model Deployment
During experiment tracking RMSE in `fare_amount` was around `4` for `XGBOOST.bin`, so we deploy this model as a flask application. The `prediction_service` contains all the files for model deployment. The service can be containerized by building Docker image from available Dockerfile in the directory.

#### Command to build Docker image of the service
`$ docker build -t nyc-taxi-fare-prediction:v1 . `

#### Command to run the service
`$ docker run -it --rm -p 9696:9696 nyc-taxi-fare-prediction:v1 `

## Testing
Few unit tests and integration test are performed so as to follow the best engineering practices.
