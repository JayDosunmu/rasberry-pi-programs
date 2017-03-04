#import Adafruit_MCP3008
import math
import pyrebase
import RPi.GPIO as GPIO
import time

config = {
        "apiKey":"AlzaSyBcPkjp50hVFQj3jL7NdCMul0Cw9jP5gkc",
        "authDomain":"hacktech-12dad.firebaseapp.com",
        "databaseURL":"https://hacktech-12dad.firebaseio.com",
        "storageBucket":"",
    }

fb = pyrebase.initialize_app(config)
db = fb.database()

sentinel = 0

CLK = 18
MISO = 23
MOSI = 24
CS = 25
#mcp = Adafruit_MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

try:
    while True:
        data = {
                "dataset":{
                    "x":sentinel,
                    "y":0.5*math.cos(sentinel)

                    },
            }
        db.child("data").set(data)
        sentinel+=.5
        time.sleep(1)
        
except KeyboardInterrupt:
    #GPIO.cleanup()
    pass
    
