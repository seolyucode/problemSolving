'''
/ ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
Problem: 131
User: seolyu
Language: Python3
Result: Success
Time: 28
ms
Memory: 25048
kb
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** /
'''

n, m = map(int, input().split())

if n > m:
    for i in range(m, n + 1):
        print(i, end=' ')
else:
    for i in range(n, m + 1):
        print(i, end=' ')

'''
x, y = list(map(int, input().split()))
if x < y:
    for i in range(x, y + 1):
        print(i, end=' ')
else:
    for i in range(y, x + 1):
        print(i, end=' ')

'''