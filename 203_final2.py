import RPi.GPIO as GPIO
import time
import os
import threading

MAGNET_GPIO = 17
startCount = 0
pre_state = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(MAGNET_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def play():
	os.system("/home/pi/start.sh")

playThread = threading.Thread(target=play)

while True:
	input_state = GPIO.input(MAGNET_GPIO)
	if input_state == 0:
		if pre_state == 1:
			if startCount == 0:
				playThread.start()
				startCount += 1
			else:
				os.system("dbuscontrol.sh pause")
		elif pre_state ==0:
			pass
	elif input_state == 1:
		if pre_state == 0:
			os.system("dbuscontrol.sh pause")
		elif pre_state == 1:
			pass
	pre_state = input_state
