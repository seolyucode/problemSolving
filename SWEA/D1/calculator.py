# 1938. 아주 간단한 계산기

import math
a, b = map(int, input().split())
 
print(a+b)
print(a-b)
print(a*b)
c = math.floor(a/b)
print (c)