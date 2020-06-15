'''
/ ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
Problem: 544
User: seolyu
Language: Python3
Result: Success
Time: 29
ms
Memory: 25048
kb
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** /
'''

N = int(input())

sum1 = 0
for i in range(1, N):
    sum1 += i

sum2 = 0
for i in range(1, 101):
    sum2 += i

print(sum2 - sum1)


# N = int(input())
#
# sum = 0
# for i in range(N, 101):
#     sum += i
#
# print(sum)