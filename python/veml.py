import time
import board
import busio
import adafruit_veml6075
i2c = busio.I2C(board.SCL, board.SDA)
veml = adafruit_veml6075.VEML6075(i2c, integration_time=100)

print('{')
print('"UVA": %0.2f,' % veml.uva)
print('"UVB": %0.2f,' % veml.uvb)
print('"UVI": %0.6f' % veml.uv_index)
print('}')
