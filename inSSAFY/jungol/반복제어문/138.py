'''
/ ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
Problem: 138
User: seolyu
Language: Python3
Result: Success
Time: 51
ms
Memory: 25960
kb
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** /
'''

N = int(input())

for i in range(1, N + 1):
    for j in range(1, N + 1):
        print("(", i, ',', sep='', end=' ')
        print(j, ')', sep='', end=' ')
    print()

'''
size = int(input())
 
for i in range(1, size + 1):
    for j in range(1, size + 1):
        # t = '(' + str(i) + ', ' + str(j) + ')'
        # print(t, end = ' ')
        print("(%d, %d)"%(i, j), end = ' ')
    print()
'''