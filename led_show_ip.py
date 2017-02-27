import socket
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Pins for each IP position
ip_pins = [6, 13, 19]

# Pins for display numbers with 3 digits
num_pins = [16, 20, 21]

for pin in ip_pins:
    GPIO.setup(pin, GPIO.OUT)

for pin in num_pins:
    GPIO.setup(pin, GPIO.OUT)

def led_on(led_pin):
    GPIO.output(led_pin, GPIO.HIGH)

def led_off(led_pin):
    GPIO.output(led_pin, GPIO.LOW)

def blink_led(led_pin):
    led_off(led_pin)
    time.sleep(0.05)
    led_on(led_pin)
    time.sleep(0.5)
    led_off(led_pin)
    time.sleep(0.3)

def flash_all():
    reset_leds()
    for i in xrange(3):
        light_all()
        time.sleep(0.2)
        reset_leds()
        time.sleep(0.1)

def reset_leds():
    map(led_off, (ip_pins+num_pins))

def light_all():
    map(led_on, (ip_pins+num_pins))

# num must be string
def display_num(num):
    for i in xrange(len(num)):
        for j in xrange(int(num[i])):
            blink_led(num_pins[i])

def display_ip_section(section, num):
    reset_leds()
    if section == 3:
        map(led_on, ip_pins)
    else:
        led_on(ip_pins[section])
    time.sleep(0.1)
    display_num(num)

def display_ip(ip_string):
    ip_nums = ip_string.split('.')
    for i in xrange(len(ip_nums)):
        display_ip_section(i, ip_nums[i])
        time.sleep(0.7)

def cleanup():
    GPIO.cleanup()

def get_ip_address():
    ip = [l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0]
    return ip

if __name__ in "__main__":
    try:
        while True:
            ip_string = get_ip_address()
            flash_all()
            print(ip_string)
            display_ip(ip_string)
            time.sleep(1.5)
    except KeyboardInterrupt:
        cleanup()
        
        
