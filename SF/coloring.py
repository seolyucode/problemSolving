T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = [[0 for i in range(N)] for j in range(N)]

    for i in range(M):
        start_x, start_y, end_x, end_y = map(int, input().split())

        for a in range(start_x-1, end_x):
            for b in range(start_y-1, end_y):
                if board[a][b] == 0:
                    board[a][b] += 1

    sum = 0
    for i in range(N):
        for j in range(N):
           if board[i][j] == 1:
               sum += 1

    print('#{} {}'.format(tc, sum))