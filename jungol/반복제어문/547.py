'''
/ ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
Problem: 547
User: seolyu
Language: Python3
Result: Success
Time: 26
ms
Memory: 25048
kb
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** /
'''

lst = [[0] * 5 for i in range(5)]

for i in range(5):
    for j in range(5):
        lst[i][j] = i + 2 + j

for i in range(len(lst)):
    for j in range(len(lst[0])):
        print(lst[i][j], end=' ')
    print()

'''
for i in range(2, 7):
    for j in range(5):
        print(i + j, end = ' ')
    print()
'''