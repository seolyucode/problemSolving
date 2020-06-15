# 2805. 농작물 수확하기

import sys
sys.stdin = open('crop_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    crop = [list(map(int, input())) for _ in range(N)]

    sum1 = 0
    for i in range(N//2):
        for k in range(N//2-i, N//2+i+1):
            sum1 += crop[i][k]

    sum2 = 0
    for j in range(N):
        sum2 += crop[N//2][j]

    sum3 = 0
    for i in range(N//2+1, N):
        for k in range(i-N//2, 3*(N//2)-i+1):
            sum3 += crop[i][k]

    print("#{} {}".format(tc, (sum1 + sum2 + sum3)))