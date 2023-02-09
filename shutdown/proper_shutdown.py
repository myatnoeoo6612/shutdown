import RPi.GPIO as GPIO
import os
import time

power_button_pin = 23
reset_button_pin = 24
##LED_PIN = 13
GPIO.setmode(GPIO.BCM)

GPIO.setup(power_button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(reset_button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
##GPIO.setup(LED_PIN, GPIO.OUT)

previous_power_button_state = GPIO.input(power_button_pin)
previous_reset_button_state = GPIO.input(reset_button_pin)

try:
    while True:
        time.sleep(0.1)
        ##time.sleep(60)
  ##     GPIO.output(LED_PIN, GPIO.HIGH)
        power_button_state = GPIO.input(power_button_pin)
        reset_button_state = GPIO.input(reset_button_pin)
        
        if power_button_state != previous_power_button_state:
            previous_power_button_state = power_button_state
            if power_button_state == GPIO.HIGH:
                print("Power Button Released!")
                time.sleep(3)
                os.system("sudo shutdown -h now")
                
        if reset_button_state != previous_reset_button_state:
            previous_reset_button_state = reset_button_state
            if reset_button_state == GPIO.HIGH:
                print("Reset Button Released!")
                time.sleep(3)
                os.system("sudo shutdown -r now")      
                
except KeyboardInterrupt:
    GPIO.clearup()
    
                      
                
                