import serial

class Ser:
    def __init__(self):
        sp = serial.Serial('/dev/ttyUSB0', 9600)

    def move(motor, deg):
        self.sp.write(f'#{motor} P{deg}\r'.encode())

    def idle():
        for i in range(6):
            self.move(i, 1500)

    def cl():
        self.sp.close()
