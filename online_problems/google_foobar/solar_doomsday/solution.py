#Inputs:
#    (int) area = 12
#Output:
#    (int list) [9, 1, 1, 1]
#
#Inputs:
#    (int) area = 15324
#Output:
#    (int list) [15129, 169, 25, 1]
#    

import math

def answer(area):
    squares = []
    while(area > 0):
        max_size = math.floor(math.sqrt(area))
        max_area = int(math.pow(max_size, 2))
        area = area - max_area
        squares.append(max_area)
        
    return squares
        
print answer(12)
print answer(15324)