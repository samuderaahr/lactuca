import time
import board
import busio
import adafruit_veml6075
import json

i2c = busio.I2C(board.SCL, board.SDA)
veml = adafruit_veml6075.VEML6075(i2c, integration_time=100)

output ={
  "ts" : int(time.time()),
  "uva": round(veml.uva, 2),
  "uvb": round(veml.uvb, 2),
  "uvi": round(veml.uv_index, 2),
}

outjson = json.dumps(output)
print(outjson)
