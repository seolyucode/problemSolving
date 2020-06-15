'''
/ ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
Problem: 132
User: seolyu
Language: Python3
Result: Success
Time: 30
ms
Memory: 25176
kb
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** /
'''

n = int(input())

lst = []
for i in range(1, n + 1):
    if i % 5 == 0:
        lst.append(i)

print(sum(lst))

'''
x = int(input())
sum = 0
for i in range(1, x + 1):
    if i % 5 == 0:
        sum += i
print(sum)
'''