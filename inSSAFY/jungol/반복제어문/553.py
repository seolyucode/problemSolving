'''
/ ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
Problem: 553
User: seolyu
Language: Python3
Result: Success
Time: 22
ms
Memory: 25048
kb
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** /
'''

n = int(input())

s = 65
for i in range(n, 0, -1):
    for j in range(i):
        print(chr(s + j), end='')
    s += i
    print()

'''
n = int(input())
 
s = 65
for i in range(n, 0, -1):
    for j in range(i):
        print(chr(s), end='')
        s += 1
    print()
'''