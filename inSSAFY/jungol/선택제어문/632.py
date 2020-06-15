'''
/**************************************************************
    Problem: 632
    User: seolyu
    Language: Python3
    Result: Success
    Time:36 ms
    Memory:25176 kb
****************************************************************/
'''
 
n1, n2, n3 = map(int, input().split())
 
lst = [n1, n2, n3]
smallest = n1
for i in lst:
    if i < smallest:
        smallest = i
print(smallest)

'''
x, y, z = list(map(int, input().split()))
if x < y:
    if x < z:
        print(x)
    else:
        print(z)
else:
    if y < z:
        print(y)
    else:
        print(z)
'''