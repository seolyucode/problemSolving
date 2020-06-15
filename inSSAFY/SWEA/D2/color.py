# 4836. [파이썬 S/W 문제해결 기본] 2일차 - 색칠하기

T = int(input())

for tc in range(1, T+1):
    zero = [[0 for i in range(10)] for i in range(10)]
    N = int(input())
    for i in range(N):
        start_x, start_y, end_x, end_y, num = map(int, input().split())
        for x in range(start_x, end_x+1):
            for y in range(start_y, end_y+1):
                if num == 1:
                    if zero[x][y] != 1:
                        zero[x][y] += num
                if num == 2:
                    if zero[x][y] != 2:
                        zero[x][y] += num

    count = 0
    for x in range(10):
        for y in range(10):
            if zero[x][y] == 3:
                count += 1

    print("#", tc, sep='', end=' ')
    print(count)