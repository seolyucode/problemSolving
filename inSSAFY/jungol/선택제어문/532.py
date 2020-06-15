'''
/**************************************************************
    Problem: 532
    User: seolyu
    Language: Python3
    Result: Success
    Time:33 ms
    Memory:25048 kb
****************************************************************/
'''
 
n1, n2 = map(float, input().split())
 
if n1 >= 4.0 and n2 >= 4.0:
    print ('A')
elif n1 >= 3.0 and n2 >= 3.0:
    print ('B')
else:
    print ('C')

'''
x, y = list(map(float, (input().split())))
 
if x >= 4.0 and y >= 4.0:
    print("A")
elif x >= 3.0 and y >= 3.0:
    print("B")
else:
    print("C")
'''