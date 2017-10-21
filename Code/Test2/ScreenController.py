import lcd_16x2_backlight as lcd


class ScreenController:

	def __init__(self):
		lcd.lcd_init()

	def setText(self, message):
		lcd.lcd_string("It's a ...", lcd.LCD_LINE_1, 1);
		lcd.lcd_string(message, lcd.LCD_LINE_2, 2);

	def setLCDToGum(self):
		self.setText("GUMBALL")

	def setLCDToWood(self):
		self.setText("WOODEN BALL")

	def setLCDToMarble(self):
		self.setText("MARBLE")
