'''
/ ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
Problem: 122
User: seolyu
Language: Python3
Result: Success
Time: 28
ms
Memory: 25176
kb
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** /
'''

year = int(input())

if year % 400 == 0:
    print('leap year')
elif year % 4 == 0 and year % 100 != 0:
    print('leap year')
else:
    print('common year')

'''
year = int(input())
 
if year % 400 == 0 :
    print('leap year')
elif year % 4 == 0 and year % 100 != 0:
    print('leap year')
else:
    print('common year')

'''