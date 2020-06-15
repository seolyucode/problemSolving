'''
/ ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
Problem: 128
User: seolyu
Language: Python3
Result: Success
Time: 32
ms
Memory: 25048
kb
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** /
'''

lst1 = list(map(int, input().split()))
lst2 = []

for i in lst1:
    if i == 0:
        print(len(lst2))
        break
    elif i % 3 == 0 or i % 5 == 0:
        continue
    else:
        lst2.append(i)

'''
nums = list(map(int, input().split()))
cnt = 0
for i in range(len(nums)):
    if not (nums[i] % 3 == 0 or nums[i] % 5 == 0):
        cnt += 1
 
print(cnt)
'''