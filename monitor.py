#!/usr/bin/python
import sys
import Adafruit_DHT
import requests
import datetime
import urllib

print("Launching temperature monitoring....")

# API Endpoint
api_endpoint = "http://192.168.0.60:8085/api/v1/set"
# Sensor definition
dht11_sensor = Adafruit_DHT.DHT22
# GIPO PIN number
data_pin = 4

# Forever!
while True:
    try:
        # Read in the humidity and temperature.
        humidity, temperature = Adafruit_DHT.read_retry(dht11_sensor, data_pin)
        try:
            # Get the current time 
            now = datetime.datetime.now()
            # Define our parameters
            params = urllib.urlencode({
                "temp": temperature,
                "hmid": humidity,
                "time": now
            })
            # Make a request to the endpoint.
            res = requests.get('', params=params);  
        except:
            print("Error when connecting to endpoint")
    except:
        print("There was an error when getting the data")
    
       
                                                                                                                                             20,12         All