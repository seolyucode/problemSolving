'''
/ ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
Problem: 137
User: seolyu
Language: Python3
Result: Success
Time: 27
ms
Memory: 25176
kb
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** /
'''

n, m = map(int, input().split())

for i in range(1, n + 1):
    for j in range(m):
        print(i + i * j, end=' ')
    print()

'''
r, c = list(map(int, input().split()))
 
for i in range(1, r + 1):
    for j in range(1, c + 1):
        print(i * j, end = ' ')
    print()

'''