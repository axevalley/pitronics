import RPi.GPIO as gpio

class PWM_LED():
	def __init__(self, pin, power=100.0, freq=50):
		self.pin = pin
		self.power = power
		self.freq = freq
		gpio.setup(self.pin, gpio.OUT, initial=0)
		self.on = False
		self.pwm = gpio.PWM(self.pin, self.freq)
		
	def turn_on(self):
		self.pwm.start(self.power)
			
			
	def turn_off(self):
		self.pwm.stop()
			
	def toggle(self):
		gpio.output(self.pin, not gpio.input(self.pin))
		
	def set_power(self, power):
		self.power = power
		self.pwm.start(self.power)
