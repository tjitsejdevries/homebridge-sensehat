#!/usr/bin/python
from sense_hat import SenseHat
import os


def get_cpu_temp():
    res = os.popen('vcgencmd measure_temp').readline()
    return float(res.replace("temp=", "").replace("'C\n", ""))


def get_temp(sense):
    t1 = sense.get_temperature_from_humidity()
    t2 = sense.get_temperature_from_pressure()
    t = (t1 + t2) / 2
    return t

sense = SenseHat()

humidity = sense.get_humidity()
pressure = sense.get_pressure()

print("%s %s %s" % (get_temp(sense), humidity, pressure))
