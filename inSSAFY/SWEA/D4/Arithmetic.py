# 1232. [S/W 문제해결 기본] 9일차 - 사칙연산

import sys
sys.stdin = open('Arithmetic_input.txt', 'r')

def arithmetic(T):
    if T:
        if tree[T][2] == '+':
            return arithmetic(int(tree[T][0])) + arithmetic(int(tree[T][1]))
        elif tree[T][2] == '-':
            return arithmetic(int(tree[T][0])) - arithmetic(int(tree[T][1]))
        elif tree[T][2] == '/':
            return arithmetic(int(tree[T][0])) / arithmetic(int(tree[T][1]))
        elif tree[T][2] == '*':
            return arithmetic(int(tree[T][0])) * arithmetic(int(tree[T][1]))
        else:
            return int(tree[T][2])

for tc in range(1, 11):
    n = int(input())

    templ = [list(input().split()) for _ in range(n)]

    tree = [[0] * 3 for _ in range(n + 1)]

    for i in range(n):
        parent = int(templ[i][0])
        if len(templ[i]) == 4:
            child_left = int(templ[i][2])
            child_right = int(templ[i][3])
            node_value = templ[i][1]

            tree[parent][0] = child_left
            tree[parent][1] = child_right
            tree[parent][2] = node_value
        else:
            node_value = int(templ[i][1])

            tree[parent][2] = node_value

    print("#{}".format(tc), end=' ')
    print(int(arithmetic(1)))