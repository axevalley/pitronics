import RPi.GPIO as GPIO
import time

from . outpin import OutPin as OutPin

class LCD:
    def __init__(self, width=16, pin_rs=18, pin_e=23, pin_d4=25, pin_d5=16, pin_d6=12, pin_d7=20, pin_led=None):
        
        GPIO.setmode(GPIO.BCM)
        
        self.width = width
        self.delay = 0.0005
        
        self.pin_rs = OutPin(pin_rs)
        self.pin_e = OutPin(pin_e)
        self.pin_d4 = OutPin(pin_d4)
        self.pin_d5 = OutPin(pin_d5)
        self.pin_d6 = OutPin(pin_d6)
        self.pin_d7 = OutPin(pin_d7)
        
        self.char = True
        self.cmd = False
        
        self.line_1 = 0x80 # LCD RAM address for the 1st line
        self.line_2 = 0xC0 # LCD RAM address for the 2nd line
        
        self.send_byte(0x33, self.cmd) # 110011 Initialise
        self.send_byte(0x32, self.cmd) # 110010 Initialise
        self.send_byte(0x06, self.cmd) # 000110 Cursor move direction
        self.send_byte(0x0C, self.cmd) # 001100 Display On,Cursor Off, Blink Off
        self.send_byte(0x28, self.cmd) # 101000 Data length, number of lines, font size
        self.send_byte(0x01, self.cmd) # 000001 Clear display
        time.sleep(self.delay)
        
    def send_byte(self, bits, mode):
        # Send byte to data pins
        # bits = data
        # mode = True  for character
        #        False for command
       
        self.pin_rs, mode # RS
       
        # High bits
        self.pin_d4.low()
        self.pin_d5.low()
        self.pin_d6.low()
        self.pin_d7.low()
        if bits&0x10 == 0x10:
            self.pin_d4.high()
        if bits&0x20 == 0x20:
            self.pin_d5.high()
        if bits&0x40 == 0x40:
            self.pin_d6.high()
        if bits&0x80 == 0x80:
            self.pin_d7.high()
       
        # Toggle 'Enable' pin
        lcd_toggle_enable()
       
        # Low bits
        self.pin_d4.low()
        self.pin_d5.low()
        self.pin_d6.low()
        self.pin_d7.low()
        if bits&0x01==0x01:
            self.pin_d4.high()
        if bits&0x02==0x02:
            self.pin_d5.high()
        if bits&0x04==0x04:
            self.pin_d6.high()
        if bits&0x08==0x08:
            self.pin_d7.high()
       
        # Toggle 'Enable' pin
        self.toggle
        
    def toggle(self):
        # Toggle enable
        time.sleep(self.delay)
        self.pin_e.high()
        time.sleep(self.delay)
        self.pin_e.low()
        time.sleep(self.delay)
        
    def write(string, line):
        # Send string to display
       
        string = string.ljust(self.width ," ")
       
        self.send_byte(line, self.cmd)
       
        for i in range(self.width):
            self.send_byte(ord(string[i]),self.char)