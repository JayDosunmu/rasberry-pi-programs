import pyrebase
import time
import sensor_api

period = 0.02
config = {
        "apiKey":"AlzaSyBcPkjp50hVFQj3jL7NdCMul0Cw9jP5gkc",
        "authDomain":"hacktech-12dad.firebaseapp.com",
        "databaseURL":"https://hacktech-12dad.firebaseio.com",
        "storageBucket":"",
    }

fb = pyrebase.initialize_app(config)
db = fb.database()

heart = HeartBeatSensor(1)
temp = TempSensor(2)
flex = FlexSensor(3)
acc = AccelSensor(0x1D)

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
                    'orientation':acc.orientation()
                },
            'heartbeat':{
                    'raw':heart.readRaw(),
                },
            'flex':{
                    'raw':heart.readRaw(),
                },
            'temp':{
                    'raw':heart.readRaw(),
                }
            }
        if seconds > 1:
            db.child('live').push(data)
            seconds = 0

        seconds += period
        time.sleep(period)

except KeyboardInterrupt:
    pass
