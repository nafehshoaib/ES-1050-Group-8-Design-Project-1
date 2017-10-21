import pigpio
import time


class ServoController:
	servo1 = 13
	servo2 = 19
	servo3 = 26

	pi = pigpio.pi()

	def setServoAtAngle(self, servo, angle):
		pulse = 0
		if servo == self.servo1:
			pulse = 5*angle + 600.
		elif servo == self.servo2:
			pulse = 5*angle + 600.
		else:
			pulse = 10*angle + 550.
		self.pi.set_servo_pulsewidth(servo, pulse)


	def openExample(self):
		self.setServoAtAngle(self.servo1, 0);
		time.sleep(1);
		self.setServoAtAngle(self.servo2, 0);
		time.sleep(1);
		self.setServoAtAngle(self.servo3, 0);
		time.sleep(1);

	def openGum(self):
		# TODO: Setup pathway for Gumball

	def openWood(self):
		# TODO: Setup pathway for Wooden Ball

	def openMarble(self):
		# TODO: Setup pathway for Marble
