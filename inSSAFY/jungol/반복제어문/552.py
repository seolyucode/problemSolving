'''
/ ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
Problem: 552
User: seolyu
Language: Python3
Result: Success
Time: 25
ms
Memory: 25048
kb
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** /
'''

n = int(input())

for i in range(n, 0, -1):
    print(' ' * (n - i), end='')
    print('*' * (2 * i - 1))

'''
n = int(input())
 
for i in range(n):
    for j in range(i):
        print(' ', end='')
    for j in range(n * 2 - 1 - i * 2):
        print('*', end='')
    print()
'''