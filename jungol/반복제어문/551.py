'''
/ ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
Problem: 551
User: seolyu
Language: Python3
Result: Success
Time: 23
ms
Memory: 25044
kb
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** /
'''

n = int(input())

for i in range(n, 0, -1):
    print(' ' * (n - i), end='')
    print('*' * i)

'''
n = int(input())
 
for i in range(n, 0, -1):
    for j in range(n-i):
        print(" ", end='')
    for j in range(i):
        print("*", end='')
    print()
'''