'''
/ ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
Problem: 549
User: seolyu
Language: Python3
Result: Success
Time: 25
ms
Memory: 25048
kb
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** /
'''

N = int(input())

for n in range(N):
    if n * n >= N:
        print(n, n * n)
        break

'''
n = int(input())
 
sum = oddcnt = 0
 
i = 1
while sum < n:
    if i % 2 == 1:
        sum += i
        oddcnt += 1
    i += 1
print(oddcnt, sum)
'''