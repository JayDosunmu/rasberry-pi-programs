import serial

ser = serial.Serial('/dev/ttyACM0', 9600)

while True:
    blink = input('How many times do you want to blink?')
    ser.write(str(blink))
    print "blinking!"
