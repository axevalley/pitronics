import RPi.GPIO as gpio
import time

from . outpin import OutPin as OutPin
from . clock import Clock as Clock

		
class ShiftRegister():
	def __init__(self, srclk=16, srclr=12, ser=18, rclk=22, registers=1, bits = 8):
		self.registers = registers
		self.bits = bits
		self.total_bits = bits * registers
		self.limit = self.max_number(self.total_bits)
		
		self.srclk = Clock(srclk)
		self.srclr = OutPin(srclr)
		self.ser = OutPin(ser)
		self.rclk = Clock(rclk)
		
		self.srclr.high()
		self.ser.low()
		self.srclk.low()
		self.rclk.low()
		
	def max_number(self, bits):
		number = ''
		for i in range(bits):
			number = number + '1'
		return int(number, 2)


	def clear(self):
		self.srclk.low()
		self.srclr.high()
		self.srclr.low()
		self.srclr.high()
		self.rclk.cycle()
		
	def push(self, binary_digit):
		self.srclr.high()
		self.srclk.low()
		self.rclk.low()
		if int(binary_digit) == 0:
			self.ser.low()
		elif int(binary_digit) == 1:
			self.ser.high()
		self.srclk.cycle()
		self.rclk.cycle()


	def write_array(self, pins):
		#self.clear()
		self.srclr.high()
		self.srclk.low()
		
		#print(pins)
	
		for pin in reversed(pins):
			#print(pin)
			if int(pin) == 1:
				self.ser.high()
				#print('high')
			elif int(pin) == 0:
				self.ser.low()
				#print('low')
			self.srclk.cycle()
		
		self.rclk.cycle()
		
	def write_bin(self, number):
		assert(number <= self.limit)
		format_string = '{:0' + str(self.total_bits) +'b}'
		bit_number = self.bits * self.registers
		bin_number = format_string.format(number)
		#print(bin_number)
		output_array = list(bin_number)
		#print(output_array)
		self.write_array(output_array)
		
	def write(self, input):
		if isinstance(input, int):
			self.write_bin(input)
		elif isinstance(input, list):
			self.write_array(input)
