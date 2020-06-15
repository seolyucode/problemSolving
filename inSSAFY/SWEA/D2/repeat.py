# 4873. [파이썬 S/W 문제해결 기본] 4일차 - 반복문자 지우기

T = int(input())

for tc in range(1, T+1):
    str = input()
    str_stack = []
    for i in range(len(str)):
        if str_stack==[] or str[i]!=str_stack[-1]:
            str_stack.append(str[i])
        elif str[i]==str_stack[-1]:
            str_stack.pop()

    print('#{} {}'.format(tc, len(str_stack)))
