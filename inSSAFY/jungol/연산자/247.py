'''
/**************************************************************
    Problem: 247
    User: seolyu
    Language: Python3
    Result: Success
    Time:28 ms
    Memory:25176 kb
****************************************************************/
''' 
 
n1, n2, n3 = map(int, input().split())
 
if n1==0 or n2==0 or n3==0:
    print (0)
else:
    print (1)

'''
n1, n2, n3 = map(int, input().split())

print(int(n1 != 0 and n2 != 0 and n3 != 0))
#print(int(bool(n1 and n2 and n3)))
'''