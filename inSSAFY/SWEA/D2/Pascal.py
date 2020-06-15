# 2005. 파스칼의 삼각형

import sys
sys.stdin = open('pascal_input.txt', 'r')

def pascal_func(N):
    for i in range(N):
        pascal[i][0] = 1
        for j in range(N):
            if i == j:
                pascal[i][j] = 1
            else:
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
    return pascal

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    pascal = [[0] * N for _ in range(N)]

    pascal = pascal_func(N)

    print("#{}".format(tc))

    for i in range(N):
        for j in range(N):
            if pascal[i][j] != 0:
                print(pascal[i][j], end=' ')
        print()