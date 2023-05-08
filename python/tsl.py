import board
import busio
import adafruit_tsl2561
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_tsl2561.TSL2561(i2c)

print('{')
print('"Lux": {:.2f},'.format(sensor.lux))
print('"Vis": {},'.format(sensor.broadband))
print('"IR": {}'.format(sensor.infrared))
print('}')
