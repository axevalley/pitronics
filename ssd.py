from . shift_register import ShiftRegister as ShiftRegister

class SSD(ShiftRegister):

    def __init__(self, displays=1, srclk=16, srclr=12, ser=18, rclk=22):
        self.displays = displays
        super(SSD, self).__init__(srclk=srclk, srclr=srclr, ser=ser, rclk=rclk, registers=self.displays, bits=8)
        
