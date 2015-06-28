from . outpin import OutPin as OutPin

class Clock(OutPin):
	def __init__(self, pin):
		self.pin = pin
		super().__init__(pin)
		
	def cycle(self):
		self.high()
		self.low()
		
