'''
/ ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
Problem: 550
User: seolyu
Language: Python3
Result: Success
Time: 42
ms
Memory: 25048
kb
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** /
'''

n = int(input())

for i in range(n, 0, -1):
    print('*' * i)
for i in range(1, n + 1):
    print('*' * i)

'''
n = int(input())
 
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end='')
    print()
     
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end = '')
    print()
'''