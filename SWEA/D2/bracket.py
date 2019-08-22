# 4866. [파이썬 S/W 문제해결 기본] 4일차 - 괄호검사

T = int(input())

for tc in range(1, T+1):
    str = input()

    lst = []
    for i in str:
        if i == '(' or i == '{':
            lst.append(i)
        elif i == ')' or i == '}':
            if len(lst) == 0:
                lst.append(i)
                break
            elif i == ')' and lst[-1] != '(':
                lst.append(i)
                break
            elif i == '}' and lst[-1] != '{':
                lst.append(i)
                break
            else:
                lst.pop()

    if lst != []:
        print('#{} {}'.format(tc, 0))
    else:
        print('#{} {}'.format(tc, 1))
