# 4874. [파이썬 S/W 문제해결 기본] 5일차 - Forth

T = int(input())

for tc in range(1, T+1):
    forth = list(input().split())
    operators = ['+', '-', '*', '/']

    stack = []
    for i in forth:
        if i == '.':
            if stack == [] or len(stack) > 1:
                print("#{} {}".format(tc, 'error'))
            else:
                print("#{} {}".format(tc, stack[0]))
        elif i not in operators and i != '.':
            stack.append(i)
        elif i in operators:
            if stack == [] or len(stack) == 1:  # len(stack) < 2
                print("#{} {}".format(tc, 'error'))
                break
            elif i == '+':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(a + b)
            elif i == '-':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b - a)
            elif i == '*':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(a * b)
            elif i == '/':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b // a)