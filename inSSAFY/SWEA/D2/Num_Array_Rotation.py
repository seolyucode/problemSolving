# 1961. 숫자 배열 회전

import sys
sys.stdin = open('Num_Array_Rotation_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    Narray = [list(map(int, input().split())) for i in range(N)]

    Narray90 = [[0]*N for i in range(N)]
    for i in range(N):
        for j in range(N):
            Narray90[j][N-1-i] = Narray[i][j]

    Narray180 = [[0]*N for i in range(N)]
    for i in range(N):
        for j in range(N):
            Narray180[N-1-i][N-1-j] = Narray[i][j]

    Narray270 = [[0]*N for i in range(N)]
    for i in range(N):
        for j in range(N):
            Narray270[N-1-j][i] = Narray[i][j]

    print('#{}'.format(tc))
    for i in range(N):
        print(''.join(map(str, Narray90[i])), ''.join(map(str, Narray180[i])), ''.join(map(str, Narray270[i])))
        # print(''.join(Narray90[i]), ''.join(Narray180[i]), ''.join(Narray270[i]))
        # TypeError: sequence item 0: expected str instance, int found

