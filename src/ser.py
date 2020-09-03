import serial

class Ser:
    def __init__(self, side):
        self.sp = serial.Serial('/dev/ttyUSB0', 9600)
        self.side = side

    def __sq_to_num(self, sq):
        if self.side == 'w':
            for num + 1, letter in enumerate(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']):
                if sq[0] == letter:
                    i = num
                    break
            
            return i, sq[1]
    
    def move(self, motor, deg):
        self.sp.write(f'#{motor} P{deg}\r'.encode())

    def idle(self):
        for i in range(6):
            self.move(i, 1500)

    def move_to_coordinate(self, uci, height):
        coord = [__sq_to_num(uci[:2]), __sq_to_num(uci[2:4])]
        print(coord)

    def remove_piece(self, square, height):
        pass

    def cl(self):
        self.sp.close()
