'''
/ ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
Problem: 540
User: seolyu
Language: Python3
Result: Success
Time: 32
ms
Memory: 25048
kb
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** /
'''

# while (True):
#     num = int(input())
#
#     if num == -1:
#         break
#     else:
#         if num % 3 != 0:
#             continue
#         else:
#             print(num // 3)


while (True):
    num = int(input())

    if num == -1:
        break
    elif num % 3 != 0:
        continue
    else:
        print(num // 3)


'''
while (True):
    x = int(input())
    if x < 0:
        break
    if x % 3 != 0:
        continue
    else:
        print(x // 3)
'''