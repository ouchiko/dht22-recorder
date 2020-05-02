#!/usr/bin/python
import sys
import Adafruit_DHT
import requests
import datetime
import urllib
import time

print("Launching temperature monitoring....")

# API Endpoint
api_endpoint = "http://temp.webcoding.co.uk/api/v1/set"
# Sensor definition
dht11_sensor = Adafruit_DHT.DHT22
# GIPO PIN number
data_pin = 4
# debugger?
debug = (len(sys.argv)>1 and sys.argv[1] == "debug")

f = open("/var/log/temp.log","w+")

# Forever!
while True:
    try:
        
        # Read in the humidity and temperature.
        humidity, temperature = Adafruit_DHT.read_retry(dht11_sensor, data_pin)
        if (debug):
            print("temp:",temperature,"humd:",humidity)
            f.write("Sensor: temp:",temperature,"humd:",humidity)
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
            f.write("Connecting: ",api_endpoint)
            res = requests.get(api_endpoint, params=params);  
        except:
            if (debug):
                print("Error when connecting to endpoint")
                f.write("Error when connecting to endpoint")
    except:
        if (debug):
            print("There was an error when getting the data")
            f.write("There was an error when getting the data")
    time.sleep(1);

f.close()
    