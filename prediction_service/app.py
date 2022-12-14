from flask import Flask, request, jsonify
import numpy as np
import pickle
from datetime import datetime

with open("XGBOOST.bin", "rb") as f_in:
    model = pickle.load(f_in)

def add_dateparts(info):
    '''
    inputs a dictionary of record
    outputs the same dictionary with
    additional date parts
    '''
    date_time = info["pickup_datetime"]
    date_time = datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S")
    info["pickup_datetime_year"] = date_time.year
    info["pickup_datetime_month"] = date_time.month
    info["pickup_datetime_hour"] = date_time.hour
    return info


def haversine_np(lon1, lat1, lon2, lat2):
  '''calculate the great circle distance between
    two points on the earth(specified in decimal degrees)
    All args must be of equal length.
  '''
  lon1, lat1, lon2, lat2  = map(np.radians, [lon1, lat1, lon2, lat2])

  dlon = lon2 - lon1
  dlat = lat2 - lat1

  a = np.sin(dlat/2.0)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2.0)**2

  c = 2 * np.arcsin(np.sqrt(a))
  km = 6367 * c
  return km


def prepare_features(info):
    '''
    prepares the `features` for model, 
    from the raw `info`, as provided
    from the user
    '''
    features = {}
    features["passenger_count"] = info["passenger_count"]

    info = add_dateparts(info=info)
    features["pickup_datetime_month"] = info["pickup_datetime_month"]
    features["pickup_datetime_year"] = info["pickup_datetime_year"]  
    features["pickup_datetime_hour"] = info["pickup_datetime_hour"]

    lon1,lat1,lon2,lat2 = info["pickup_longitude"],info["pickup_latitude"],info["dropoff_longitude"],info["dropoff_latitude"]
    features["trip_distance"] = haversine_np(lon1,lat1,lon2,lat2)

    return features
def get_input_for_model(features):
    '''
    this function recieves a dictionary, which
    is a single record of data, and returns a 2-d 
    array suitable for model to perform prediction
    '''
    inputs = []
    for name, feat in features.items():
        inputs.append(feat)
    
    return np.array(inputs).reshape(1,-1)



app = Flask("taxi-fare-prediction")

@app.route('/predict', methods=["POST"])
def predict_endpoint():
    '''
    This is the endpoint for our prediction service
    '''
    info = request.get_json()

    features = prepare_features(info)
    inputs = get_input_for_model(features=features)
    pred = model.predict(inputs)

    result = {
        "fare_amount": float(pred)
    }
    return jsonify(result)


if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)










#input_cols = ["passenger_count","pickup_datetime_month","pickup_datetime_year","pickup_datetime_hour", "trip_distance"]
#target = "fare_amount"
