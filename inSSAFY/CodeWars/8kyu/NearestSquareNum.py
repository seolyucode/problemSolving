# Find Nearest square number

import math

def nearest_sq(n):
    num = math.sqrt(n)
    
    if round(num) == math.floor(num):
        return (math.floor(num))**2
    else:
        return (round(num))**2