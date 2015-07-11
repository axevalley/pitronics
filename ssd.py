from . shift_register import ShiftRegister as ShiftRegister

class SSD(ShiftRegister):

    def __init__(self, displays=1, srclk=16, srclr=12, ser=18, rclk=22):
        self.displays = displays
        super(SSD, self).__init__(srclk=srclk, srclr=srclr, ser=ser, rclk=rclk, registers=self.displays, bits=8)
        self.blank = [0, 0, 0, 0, 0, 0, 0, 0]
        self.digits = self.make_digits()
        
    def make_digits(self):
        digits = []
        for i in range(10):
            digits.append([])
        digits[0] = [0, 1, 1, 1, 1, 1, 1, 0]
        digits[1] = [0, 0, 0, 1, 0, 0, 1, 0]
        digits[2] = [1, 0, 1, 1, 1, 1, 0, 0]
        digits[3] = [1, 0, 1, 1, 0, 1, 1, 0]
        digits[4] = [1, 1, 0, 1, 0, 0, 1, 0]
        digits[5] = [1, 1, 1, 0, 0, 1, 1, 0]
        digits[6] = [1, 1, 1, 0, 1, 1, 1, 0]
        digits[7] = [0, 0, 1, 1, 0, 0, 1, 0]
        digits[8] = [1, 1, 1, 1, 1, 1, 1, 0]
        digits[9] = [1, 1, 1, 1, 0, 0, 1, 0]
        
        return digits
        
    def write_number(self, number):
        bits = []
                    
        for display in range(self.displays):
            if display >= len(str(number)):
                for bit in reversed(self.blank):
                    bits.insert(0, bit)
            else:
                digit = int(str(number)[-display])
                for bit in self.digits[digit]:
                    bits.append(bit)
                
        self.write(bits)
