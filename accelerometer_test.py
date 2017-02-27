import smbus
import time
import os
import math

class MMA7455():
    bus = smbus.SMBus(1)
    def __init__(self):
        self.bus.write_byte_data(0x1D, 0x16, 0x55)
        self.bus.write_byte_data(0x1D, 0x10, 0)
        self.bus.write_byte_data(0x1D, 0x11, 0)
        self.bus.write_byte_data(0x1D, 0x12, 0)
        self.bus.write_byte_data(0x1D, 0x13, 0)
        self.bus.write_byte_data(0x1D, 0x14, 0)
        self.bus.write_byte_data(0x1D, 0x15, 0)

    def getValueX(self):
        return self.bus.read_byte_data(0x1D, 0x06)

    def getValueY(self):
        return self.bus.read_byte_data(0x1D, 0x07)

    def getValueZ(self):
        return self.bus.read_byte_data(0x1D, 0x08)

mma = MMA7455()

try:
    while True:
        x = mma.getValueX()
        y = mma.getValueY()
        z = mma.getValueZ()
        x2 = ((x + 235) % 256) - 128
        y2 = ((y + 210) % 256) - 128
        z2 = ((z + 120) % 256) - 128
        mag = int(math.sqrt(x2*x2 + y2*y2 + z2*z2))
        vertangle = 180/3.142 * math.atan2(x2, math.sqrt(y2*y2 + z2*z2))
        print('x: ',x,', x2: ',x2)
        print('y: ',y,', y2: ',y2)
        print('z: ',z,', z2: ',z2)
        print('Magnitude: ',mag)
        print('Vertical Angle: ',vertangle)
        time.sleep(0.2)
        os.system('clear')
except KeyboardInterrupt:
    pass
