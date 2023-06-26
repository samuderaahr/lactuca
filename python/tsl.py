import board
import busio
import adafruit_tsl2561
import json
import time

i2c = busio.I2C(board.SCL, board.SDA)
tsl = adafruit_tsl2561.TSL2561(i2c)

output ={
  "ts": int(time.time()),
  "lux": round(tsl.lux, 2),
  "vis": round(tsl.broadband, 2),
  "IRd": round(tsl.infrared, 2)
}

outjson = json.dumps(output)
print(outjson)
