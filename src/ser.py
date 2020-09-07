import serial, time

class Ser:
    def __init__(self, side):
        self.sp = serial.Serial('/dev/ttyUSB0', 9600)
        self.side = side

    def __sq_to_num(self, sq):
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        
        if self.side == 'w':
            for num, letter in enumerate(letters):
                if sq[0] == letter:
                    i = num + 1
                    break  
            return i, sq[1]
        else:
            for num, letter in enumerate(reversed(letters)):
                if sq[0] == letter:
                    i = num + 1
                    break
            return i, 9 - sq[1]

    
    def move(self, motor, deg, speed=100):
        
        self.sp.write(f'#{motor} P{deg} S{speed}\r'.encode())

    def idle(self):
        for i in range(6):
            self.move(i, 1500, 10)
        
    def move_to_coordinate(self, uci, height):
        coord = [__sq_to_num(uci[:2]), __sq_to_num(uci[2:4])]
        print(coord)

    def remove_piece(self, square, height):
        pass

    def cl(self):
        self.sp.close()
