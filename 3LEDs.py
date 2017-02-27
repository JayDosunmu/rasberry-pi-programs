import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

pin = [16, 20, 21]
try:
    while True:
        for i in xrange(3):
            GPIO.output(pin[i], GPIO.HIGH)
            time.sleep(0.5)
        for j in xrange(3):
            GPIO.output(pin[j], GPIO.LOW)
            time.sleep(0.2)
except KeyboardInterrupt:
    GPIO.cleanup()
