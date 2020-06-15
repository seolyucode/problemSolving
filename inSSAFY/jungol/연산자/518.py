'''
/**************************************************************
    Problem: 518
    User: seolyu
    Language: Python3
    Result: Success
    Time:26 ms
    Memory:25048 kb
****************************************************************/
'''

import math
 
num = list(map(int, input().split()))
sum = 0
 
for i in num:
    sum += i
 
avg = math.floor(sum / len(num))
 
print ('sum :', sum)
print ('avg :', avg)


'''
x, y, z = map(int, input().split())
print("sum : %d"%(x + y + z))
print("avg : %d"%((x + y + z)//3))
'''