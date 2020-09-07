from math import sin, asin, acos, sqrt, degrees, atan
'''
a = 18.5
b = 15
d = 11.5
t = 7.5 + 2
'''

conv_to_servo = lambda deg: ((deg * 2000) / 180) + 500

def calc_arms(piece_height, E):
    
    '''
    p = d + piece_height
    c = sqrt(E ** 2 + (p - t) ** 2)
    C = degrees(acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b)))
    m = degrees(asin(E / c) + asin((b / c) * sin(C)))
    h = degrees(acos(a / c) + asin((a / c) * sin(C)))

    return [servo(h), servo(C), servo(m)]
    '''
    
    a = 14.75
    b = 18.5
    d = 11.5
    h = 9.5


    #theta = conv_to_servo(90 - degrees(atan((4.5 - i) / (0.5 + j))))

    #l = sqrt((4.5 - i) ** 2 + (0.5 + j) ** 2) * 5.75

    w = piece_height

    f = d + w - h

    c = sqrt(f ** 2 + E ** 2)

    gamma_2 = degrees(atan(E / f))

    alpha_1 = degrees(atan(f / E))

    gamma_3 = degrees(acos((c ** 2 + b ** 2 - a ** 2) / (2 * b * c)))

    alpha_2 = degrees(acos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c)))

    gamma = conv_to_servo(gamma_2 + gamma_3)
    beta = conv_to_servo(gamma_3 + alpha_2)
    alpha = conv_to_servo(alpha_1 + alpha_2)

    return [int(alpha), int(beta), int(gamma)]

