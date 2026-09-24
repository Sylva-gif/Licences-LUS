"""MATÉRIEL REQUIS : ESP32 + DHT22 compatible ; MicroPython, pas CPython."""

from machine import Pin
import dht
import time

sensor = dht.DHT22(Pin(4))
for _ in range(3):
    try:
        sensor.measure()
        print({"temperature": sensor.temperature(), "humidity": sensor.humidity()})
    except OSError as error:
        print({"error": str(error)})
    time.sleep(2)
