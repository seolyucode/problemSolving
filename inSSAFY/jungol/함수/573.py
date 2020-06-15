'''
/ ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
Problem: 573
User: seolyu
Language: Python3
Result: Success
Time: 33
ms
Memory: 25408
kb
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** /
'''

n = int(input())


def square(n):
    for i in range(n):
        for j in range(n):
            print(i * n + 1 + j, end=' ')
        print()


square(n)

'''
def func(n):
    for i in range(n):
        for j in range(n):
            print(i * n + j + 1, end = ' ')
        print()
 
x = int(input())
func(x)

'''