import smbus
import time
import math

import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008


SPI_PORT = 0
SPI_DEVICE = 0

mcp = Adafruit_MCP3008.MCP3008(spi = SPI.SpiDev(SPI_PORT, SPI_DEVICE))


class MCPSensor:
    def __init__(self, channel):
        self.period = 20
        self.channel = channel

    def readRaw(self):
        return mcp.read_adc(self.channel)

    def processRaw(self):
        pass
    
    def getPeriod(self):
        return self.period


class HeartbeatSensor(MCPSensor):
    alpha = 0.75
    def __init__(self, channel):
        super().__init__()
        self.new_timestamp = time.time()
        self.old_timestamp = new_timestamp

    def getBPM(self):
        return

    def update(self):
        self.new_timestamp = time.time()


class TempSensor(MCPSensor):
    def processRaw(self):
        return (self.readRaw * 5.0)/1024.0
    
    def getCelcius(self):
        return (self.processRaw() - 0.5) * 100

    def getFahrenheit(self):
        return (self.getCelcius() * 9.0/5.0) + 32.0


class FlexSensor(MCPSensor):
    def getAngle(self):
        pass


class AccelSensor:
    bus = smbus.SMBus(1)
    def __init__(self, address):
        self.period = 20
        self.address = address
        self.bus.write_byte_data(self.address, 0x16, 0x55)
        self.bus.write_byte_data(self.address, 0x10, 0)
        self.bus.write_byte_data(self.address, 0x11, 0)
        self.bus.write_byte_data(self.address, 0x12, 0)
        self.bus.write_byte_data(self.address, 0x13, 0)
        self.bus.write_byte_data(self.address, 0x14, 0)
        self.bus.write_byte_data(self.address, 0x15, 0)

    def getValueX(self):
        return self.bus.read_byte_data(self.address, 0x06)

    def getValueY(self):
        return self.bus.read_byte_data(self.address, 0x07)

    def getValueZ(self):
        return self.bus.read_byte_data(self.address, 0x08)

    def getTheta(self):
        return "unable to get theta"

    def getPsi(self):
        return "unable to get psi"

    def getMag(self):
        return math.sqrt(
                self.getValueX()*self.getValueX()+
                self.getValueY()*self.getValueY()+
                self.getValueZ()*self.getValueZ())

    def getOrientation(self):
        return 'unknown'

    def getPeriod(self):
        return self.period

