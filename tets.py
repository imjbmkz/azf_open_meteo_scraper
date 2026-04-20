import datetime as dt
import requests 
import pandas as pd
from sqlalchemy import create_engine, URL 

request_time = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Make sure all required weather variables are listed here
# The order of variables in hourly or daily is important to assign them correctly below
url = "https://api.open-meteo.com/v1/forecast"
params = {
	"latitude": 14.559571295922172,
	"longitude": 121.0165314944657,
	"current": "temperature_2m",
	"timezone": "Asia/Singapore",
}
response = requests.get(url, params = params).json()

resp_latitude = response["latitude"]
resp_longitude = response["longitude"]
resp_generationtime_ms = response["generationtime_ms"]
resp_utc_offset_seconds = response["utc_offset_seconds"]
resp_timezone = response["timezone"]
resp_timezone_abbreviation = response["timezone_abbreviation"]
resp_elevation = response["elevation"]
resp_current_time = response["current"]["time"]
resp_current_interval = response["current"]["interval"]
resp_current_temperature_2m = response["current"]["temperature_2m"]

data = {
    "request_time": request_time,
    "latitude": resp_latitude,
    "longitude": resp_longitude,
    "generationtime_ms": resp_generationtime_ms,
    "utc_offset_seconds": resp_utc_offset_seconds,
    "timezone": resp_timezone,
    "timezone_abbreviation": resp_timezone_abbreviation,
    "elevation": resp_elevation,
    "current_time": resp_current_time,
    "current_interval": resp_current_interval,
    "current_temperature_2m": resp_current_temperature_2m,
}

df = pd.DataFrame([data])
print(df)