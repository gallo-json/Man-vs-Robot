from ser import Ser
from ik import calc_arms

angles = calc_arms(4.5, 25)
print(angles)

s = Ser('w')

s.idle()
s.move(4, 500)

s.move(3, angles[2])
s.move(2, angles[1])
s.move(1, angles[0])

s.move(4,1500)

s.move(3, 1500)
s.move(2, 1500)
s.move(1, 1500)

s.cl()