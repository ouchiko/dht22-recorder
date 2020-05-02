# DHT22 Sensor and data sender

The objective is run the `DHT22` sensor via the PI and forward on the results to be stored and used.  The sensor provides accurate temperature and humidity values.

## Installation

Pretty basic, make sure we have `libgpiod2` and install the `PIP` requirements which will allow the monitoring service to run.

```
mkdir -p /srv/dht/
cd /srv/dht/
git clone git@github.com:ouchiko/dht22-recorder.git 
```

```
sudo apt-get update
sudo apt-get install -y libgpiod2
pip install -r requirements.txt
python monitor.py
```

You can run `monitor.py debug` to output temperature readings and any errors produced.

You should edit the `monitor.py` file and alter the end point to address your server correctly.

## As a service

If we create a new service in `/etc/init.d/temperature` with the following block:

```
#! /bin/bash
# /etc/init.d/temperature
#

# Carry out specific functions when asked to by the system
case "$1" in
  start)
    echo "Temp Start"
    sleep 15
    cd /srv/dht/dht22-recorder && pip install -r requirements.txt  &&  python monitor.py
    ;;
  stop)
    echo "Stopping script blah"
    echo "Could do more here"
    ;;
  *)
    echo "Usage: /etc/init.d/blah {start|stop}"
    exit 1
    ;;
esac

exit 0
```

We can find out our run level with `runlevel` and then make an entry into (for example)

```
cd /etc/rc5.d   
ln -s ../init.d/temperature S01temp
```    