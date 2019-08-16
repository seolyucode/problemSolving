'''
/ ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
Problem: 545
User: seolyu
Language: Python3
Result: Success
Time: 32
ms
Memory: 25048
kb
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** /
'''

num = list(map(int, input().split()))

mul3 = []
mul5 = []

for i in num:
    if i % 3 == 0:
        mul3.append(i)

for i in num:
    if i % 5 == 0:
        mul5.append(i)

print("Multiples of 3 :", len(mul3))
print("Multiples of 5 :", len(mul5))

'''
nums = list(map(int, input().split()))
mul3 = 0
mul5 = 0
for i in range(10):
    if nums[i] % 3 == 0:
        mul3 += 1
    if nums[i] % 5 == 0:
        mul5 += 1
print('Multiples of 3 :', mul3)
print('Multiples of 5 :', mul5)

'''