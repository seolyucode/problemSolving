'''
/ ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
Problem: 163
User: seolyu
Language: Python3
Result: Success
Time: 24
ms
Memory: 25044
kb
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** /
'''

array = [[3, 5, 9], [2, 11, 5], [8, 30, 10], [22, 5, 1]]

for i in range(4):
    for j in range(3):
        print(array[i][j], end=' ')
    print()

sum = 0
for i in range(4):
    for j in range(3):
        sum += array[i][j]

print(sum)

'''
arr = [[3, 5, 9], [2, 11, 5], [8, 30, 10], [22, 5, 1]]
 
sum = 0
for i in range(4):
    for j in range(3):
        print(arr[i][j], end = ' ')
        sum += arr[i][j]
    print()
 
print(sum)
'''