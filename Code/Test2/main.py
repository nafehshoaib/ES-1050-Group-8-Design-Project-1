# Western Engineering 2017 ES 1050 Group 8 Design Project 1
#
# Team Members: Nafeh Shoaib, Tom Keech, Travis Puhr, and Brandon Folia
#
# Required Frameworks:
# 	- PiGPIO
#	- LCD.py from RaspberryPi-Spy.co.uk
#
#
# Requirements in main.py
# 	- ServoController.py
#	- ScreenController.py


import ServoController as Servo
import ScreenController as Screen
from picamera import PiCamera

gumball = "Gumball"
woodenBall = "Wooden"
marble = "Marble"

camera = PiCamera()
cameraPath = "/home/pi/Projects/UWO"

screenController = Screen.ScreenController
servoController = Servo.ServoController

for i in range(0, 15):

	type = "Gumball"

	# Use piston to release balls one at a time.
	#TODO: Piston Code

	# Detect Type of Ball
	#TODO: Camera Code

	# Display Type on Display
	if type == "Gumball":
		screenController.setLCDToGum()
	elif type == "Wooden":
		screenController.setLCDToWood()
	else:
		screenController.setLCDToMarble()

	# Make pathway for ball
	if type == "Gumball":
		servoController.openGum()
	elif type == "Wooden":
		servoController.openWood()
	else:
		servoController.openMarble()