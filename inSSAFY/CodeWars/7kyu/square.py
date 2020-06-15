# You're a square!

import math
def is_square(n):
    if n<0:
        return False
    elif math.sqrt(n)%1:
        return False
    else:
        return True