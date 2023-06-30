
#!/usr/bin/env python3
from pyfirmata import Arduino,util
import time

board = SparkfunProMicro('/dev/ttyACM0')


while True:
    board.digital[13].write(1)
    sleep(0.5)
    board.digital[17].write(0)
