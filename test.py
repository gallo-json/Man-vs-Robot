import serial

# create and open a serial port
sp = serial.Serial('/dev/ttyUSB0', 9600)

# set the arm to default centered position
sp.write("#0 P1500\r".encode())
sp.write("#1 P1500\r".encode())
sp.write("#2 P1500\r".encode())
sp.write("#3 P1500\r".encode())
sp.write("#4 P1500\r".encode())
sp.write("#5 P1500\r".encode())