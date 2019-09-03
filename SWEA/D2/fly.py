# 2001. 파리 퇴치
import sys
sys.stdin = open("input.txt", 'r')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    NN = [list(map(int, input().split())) for _ in range(N)]

    lst = []

    for i in range(0, N-M+1):
        for j in range(0, N-M+1):
            sum = 0
            for a in range(i, i+M):
                for b in range(j, j+M):
                    sum += NN[a][b]
            lst.append(sum)

    print("#{} {}".format(tc, max(lst)))