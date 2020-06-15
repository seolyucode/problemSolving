'''
/ ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
Problem: 126
User: seolyu
Language: Python3
Result: Success
Time: 35
ms
Memory: 25048
kb
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** /
'''

num = list(map(int, input().split()))

odd_lst = []
even_lst = []

for i in num:
    if i == 0:
        print('odd :', len(odd_lst))
        print('even :', len(even_lst))
        break
    elif i % 2:
        odd_lst.append(i)
    else:
        even_lst.append(i)

'''
nums = list(map(int, input().split()))
oddcnt = 0
for i in range(len(nums)):
    if nums[i] % 2 == 1:
        oddcnt += 1
 
print('odd :', oddcnt)
print('even :', len(nums) - oddcnt - 1)
'''