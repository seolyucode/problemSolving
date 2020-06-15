T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())

    board = [[0 for j in range(M)] for i in range(N)]

    for i in range(N):
        board[i] = list(map(int, input().split()))

    lst = []
    for i in range(N-K+1):
        for j in range(M-K+1):
            sum1 = 0
            for a in range(i, i+K):
                for b in range(j, j+K):
                    sum1 += board[a][b]

            sum2 = 0
            for c in range(i+1, i+K-1):
                for d in range(j+1, j+K-1):
                    sum2 += board[c][d]
            lst.append(sum1-sum2)

    print('#{} {}'.format(tc, max(lst)))