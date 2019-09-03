# 4875. [파이썬 S/W 문제해결 기본] 5일차 - 미로

import sys
sys.stdin = open('maze_input.txt', 'r')

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def is_wall(x, y, N):
    if x < 0 or y < 0 or x >= N or y >= N:
        return True

def dfs(x, y):


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    maze = [input() for _ in range(N)]
    visited = [[False] * N for i in range(N)]

    for j in range(N):
        if maze[N-1][j] == 2:
            x, y = N-1, j
            break

    while True:
        if maze[x][y] == 3:
            result = 1
            break

        for i in range(4):
            X = x + dx[i]
            Y = y + dy[i]

            if is_wall(X, Y, N):
                break
