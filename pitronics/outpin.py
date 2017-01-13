import RPi.GPIO as gpio

class OutPin():
	def __init__(self, pin):
		self.pin = pin
		gpio.setup(self.pin, gpio.OUT)
		
	def high(self):
		gpio.output(self.pin, gpio.HIGH)
		
	def low(self):
		gpio.output(self.pin, gpio.LOW)
