'''
/**************************************************************
    Problem: 525
    User: seolyu
    Language: Python3
    Result: Success
    Time:39 ms
    Memory:25176 kb
****************************************************************/
''' 
 
n1, n2, n3 = map(int, input().split())
 
if n1 > n2 and n1 > n3:
    print (1, end = ' ')
else:
    print (0, end = ' ')
 
if n1==n2 and n1==n3:
    print(1)
else:
    print(0)

'''
n1, n2, n3 = map(int, input().split())
 
print(n1 > n2 and n1 > n3, end = ' ')
print(n1 == n2 == n3)
'''