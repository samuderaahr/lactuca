import board
import math

from adafruit_bme280 import basic as adafruit_bme280
i2c = board.I2C()
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

bme280.sea_level_pressure = 1010.1

b = 17.62
c = 243.12
gamma = (b * bme280.temperature /(c + bme280.temperature))
gammaN = gamma + math.log(bme280.humidity / 100.0)
dewpoint = (c * gammaN) / (b - gammaN)

print('{')
print('"Tmp": %0.1f,' % bme280.temperature)
print('"Hum": %0.1f,' % bme280.humidity)
print('"Prs": %0.1f,' % bme280.pressure)
print('"Alt": %0.2f,' % bme280.altitude)
print('"DwP": %0.2f' % dewpoint)
print('}')
