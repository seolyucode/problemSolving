'''
/ ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
Problem: 167
User: seolyu
Language: Python3
Result: Success
Time: 26
ms
Memory: 25048
kb
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** /
'''

import math

arr = [list(map(int, input().split())) for i in range(4)]

for i in range(4):
    print(math.floor(sum(arr[i]) / 2), end=' ')
print()

for j in range(2):
    lst1 = []
    for i in range(4):
        lst1.append(arr[i][j])
    print(math.floor(sum(lst1) / 4), end=' ')
print()

lst2 = []
for i in range(4):
    for j in range(2):
        lst2.append(arr[i][j])
print(math.floor(sum(lst2) / 8))

'''
arr = [0] * 4
 
for i in range(4):
    arr[i] = list(map(int, input().split()))
 
for i in range(4):
    t = 0
    for j in range(2):
        t += arr[i][j]
    print(t // 2, end = ' ')
print()
 
total = 0
for i in range(2):
    t = 0
    for j in range(4):
        t += arr[j][i]
    print(t // 4, end = ' ')
    total += t
print()
 
print(total // 8)
'''