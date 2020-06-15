'''
/ ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
Problem: 139
User: seolyu
Language: Python3
Result: Success
Time: 30
ms
Memory: 25176
kb
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** /
'''

N1, N2 = list(map(int, input().split()))

if N1 > N2:
    for i in range(1, 10):
        for j in range(N1, N2 - 1, -1):
            print(j, '*', i, '=', "%2d" % (i * j), end='   ')
        print()

else:
    for i in range(1, 10):
        for j in range(N1, N2 + 1):
            print(j, '*', i, '=', "%2d" % (i * j), end='   ')
        print()

'''
s, e = list(map(int, input().split()))
 
if s > e :
    for i in range(1, 10):
        for dan in range(s, e - 1, -1):
            print("%d * %d =%3d"%(dan, i, dan * i), end = '   ')
        print()
else:
    for i in range(1, 10):
        for dan in range(s, e + 1):
            print("%d * %d =%3d"%(dan, i, dan * i), end = '   ')
        print()
'''