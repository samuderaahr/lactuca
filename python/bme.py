import board
import math
import json
import time

from adafruit_bme280 import basic as adafruit_bme280
i2c = board.I2C()
bme = adafruit_bme280.Adafruit_BME280_I2C(i2c)

bme.sea_level_pressure = 1006

b = 17.62
c = 243.12
gamma = (b * bme.temperature /(c + bme.temperature))
gammaN = gamma + math.log(bme.humidity / 100.0)
dewpoint = (c * gammaN) / (b - gammaN)

output ={
  "ts" : int(time.time()),
  "tmp": round(bme.temperature, 2),
  "hum": round(bme.humidity, 2),
  "prs": round(bme.pressure, 2),
  "alt": round(bme.altitude, 2),
  "dwp": round(dewpoint, 2)
}

outjson = json.dumps(output)
print(outjson)
