import requests

info = {
        "pickup_datetime": "2013-09-17 04:22:00",
        "pickup_longitude": -73.98721,
        "pickup_latitude": 40.729324,
        "dropoff_longitude": -73.931984,
        "dropoff_latitude": 40.69721,
        "passenger_count": 1
}

url = 'http://localhost:9696/predict'
response = requests.post(url, json=info)
predicted_value = round(response.json()["fare_amount"],2)

assert predicted_value == 16.41
