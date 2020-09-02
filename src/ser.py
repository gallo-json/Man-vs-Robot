import serial

class Ser:
    def __init__(self):
        sp = serial.Serial('/dev/ttyUSB0', 9600)

    def move(self, motor, deg):
        self.sp.write(f'#{motor} P{deg}\r'.encode())

    def idle(self):
        for i in range(6):
            self.move(i, 1500)

    def cl(self):
        self.sp.close()
