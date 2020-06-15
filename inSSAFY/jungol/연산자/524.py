'''
/**************************************************************
    Problem: 524
    User: seolyu
    Language: Python3
    Result: Success
    Time:28 ms
    Memory:25044 kb
****************************************************************/
''' 
 
n1, n2 = map(int, input().split())
 
if n1 and n2:
    print (1, end=' ')
else:
    print (0, end= ' ')
 
if n1 or n2:
    print (1)
else:
    print (0)

'''
n1, n2 = map(int, input().split())

print(bool(n1 and n2)) # print(n1 and n2)
print(bool(n1 or n2))  # print(n1 or n2)
'''