import pyrebase
import time
import sensor_api
import os

period = 0.02
config = {
        "apiKey":"AlzaSyBcPkjp50hVFQj3jL7NdCMul0Cw9jP5gkc",
        "authDomain":"hacktech-12dad.firebaseapp.com",
        "databaseURL":"https://hacktech-12dad.firebaseio.com",
        "storageBucket":"",
    }

fb = pyrebase.initialize_app(config)
db = fb.database()

heart = sensor_api.HeartbeatSensor(1)
temp = sensor_api.TempSensor(2)
flex = sensor_api.FlexSensor(3)
acc = sensor_api.AccelSensor(0x1D)

seconds = 0

try:
    while True:
        data = {
            'accelerometer':{
                    'x':acc.getValueX(),
                    'y':acc.getValueX(),
                    'z':acc.getValueX(),
                    'theta':acc.getTheta(),
                    'psi':acc.getPsi(),
                    'orientation':acc.getOrientation()
                },
            'heartbeat':{
                    'raw':heart.readRaw(),
                },
            'flex':{
                    'raw':flex.readRaw(),
                },
            'temp':{
                    'C':temp.getCelcius(),
                    'F':temp.getFahrenheit(),
                }
            }
        if seconds > 1:
            #db.child('live').push(data)
            os.system('clear')
            print(data)
            
            seconds = 0

        seconds += period
        time.sleep(period)

except KeyboardInterrupt:
    pass
