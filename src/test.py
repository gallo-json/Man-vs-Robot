from ser import Ser
from ik import calc_arms
from time import sleep

angles = calc_arms(6, 25)
print(angles)

s = Ser('w')
s.idle()
sleep(2)

s.move(4, 2500)
sleep(2)

s.move(3, angles[2])
sleep(2)
s.move(2, angles[1])
sleep(0.2)
s.move(1, angles[0])
sleep(2)

s.move(4,500)
sleep(2)

s.move(3, 1500)
sleep(2)
s.move(2, 1500)
sleep(2)
s.move(1, 1500)
sleep(2)

s.cl()