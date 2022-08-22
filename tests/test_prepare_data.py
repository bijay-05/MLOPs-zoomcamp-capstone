from prepare_data import add_dateparts, add_features
import pandas as pd


df = pd.DataFrame({
    "Id": [8,9,12,59,69,70,71,76],
    "fare_amount": [8.0,19.0,7.0,31.83,5.5,8.0,17.0,6.0],
    "pickup_longitude": [0.0,-73.98721,-73.95906,-73.866135,-73.99103,-73.982155,-73.98855,-74.0027],
    "pickup_latitude": [0.0,40.729324,40.78106,40.77124,40.719547,40.76196,40.77822,40.728447],
    "dropoff_longitude": [0.0,-73.931984,-73.96206,-73.95456,-73.988396,-73.99678,-73.98224,-73.99433],
    "dropoff_latitude": [0.0,40.69721,40.768604,40.767246,40.724224,40.737362,40.75185,40.7363],
    "passenger_count": [2,1,1,1,2,1,3,1],
    "pickup_datetime": ["2013-01-17 17:22:00","2013-09-17 04:22:00","2013-11-06 11:26:54","2013-05-29 23:47:00","2013-04-21 01:28:56","2013-01-16 06:54:28","2013-06-12 17:46:00","2013-01-08 08:21:00"]
})

df = add_dateparts(df=df, col="pickup_datetime")
data_for_year = df["pickup_datetime_year"].unique()

df = add_features(df=df)
columns = list(df.columns)

assert data_for_year == 2013
assert len(columns) == 14
