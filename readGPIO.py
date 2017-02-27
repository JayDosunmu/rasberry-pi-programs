import RPi.GPIO as GPIO, time

GPIO.setmode(GPIO.BCM)

def RCtime(pin):
    measurement = 0

    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(0.1)

    GPIO.setup(pin, GPIO.IN)
    while(GPIO.input(pin) == GPIO.LOW):
        measurement += 1

    return measurement
try:
    while True:
        print RCtime(19)
except KeyboardInterrupt:
    GPIO.cleanup()
