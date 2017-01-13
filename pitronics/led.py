import RPi.GPIO as gpio

class LED():
	def __init__(self, pin):
		self.pin = pin
		gpio.setup(self.pin, gpio.OUT, initial=0)
		self.on = False
		
	def turn_on(self):
		if gpio.input(self.pin) == False:
			gpio.output(self.pin, 1)
			
	def turn_off(self):
		if gpio.input(self.pin) == True:
			gpio.output(self.pin, 0)
			
	def toggle(self):
		gpio.output(self.pin, not gpio.input(self.pin))
