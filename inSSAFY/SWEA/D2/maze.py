# 4875. [파이썬 S/W 문제해결 기본] 5일차 - 미로

import sys
sys.stdin = open('maze_input.txt', 'r')

def is_wall(x, y, N):
    if x < 0 or x >= N or y < 0 or y >= N:
        return True
    elif maze[x][y] == 1:
        return True
    else:
        return False

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    check = [[False] * N for i in range(N)]
    stack = []

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                x = i
                y = j

    while True:
        if maze[x][y] == 3:
            result = 1
            break

        for k in range(4):
            X = x + dx[k]
            Y = y + dy[k]

            if is_wall(X, Y, N) == False and check[X][Y] == False:
                stack.append([X, Y])

        if stack == []:
            result = 0
            break

        check[x][y] = True

        temp = stack.pop()
        x = temp[0]
        y = temp[1]

    print("#{} {}".format(tc, result))