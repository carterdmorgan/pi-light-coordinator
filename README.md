# Raspberry Pi Light Coordinator

A collection of python scripts to coordinate a string of LED lights connected to a Raspberry Pi using a corresponding websocket server and Angular SPA.

## Quick Start

The LED strip must be set up according to [this tutorial](https://dordnung.de/raspberrypi-ledstrip/).  Make sure to follow the steps on installing [pigpio](http://abyz.me.uk/rpi/pigpio/pigpiod.html), but they're included here as well for easy reference:.

```
sudo apt-get install build-essential unzip wget
wget http://abyz.me.uk/rpi/pigpio/pigpio.zip && unzip pigpio.zip && cd PIGPIO && sudo make install
```

Then clone this repository and run any of the python scripts.
