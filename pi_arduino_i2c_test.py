import smbus
import time

bus = smbus.SMBus(1)

address = 0x04

def writeNumber(value):
    bus.write_byte(address, value)
    return -1

def readNumber():
    number = bus.read_byte(address)
    return number

try:
    while True:
        var = input("1-9: ")
        if not var:
            continue
        
        writeNumber(var)
        print "RPi: Hi Arduino, I sent you ", var
        time.sleep(1)

        number = readNumber()
        print "Arduino: Hi Pi, I received digit ", var
        print
except KeyboardInterrupt:
    pass

