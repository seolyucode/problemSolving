# 1979. 어디에 단어가 들어갈 수 있을까

import sys
sys.stdin = open('wordpuzzle_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]

    count = 0


    # 가로
    for i in range(N):

        for j in range(N-K+1):
            check = 0
            # if check == 1:
            #     break
            if puzzle[i][j] == 1:
                # if check == 1:
                #     break
                for k in range(K):
                    if puzzle[i][j+k] == 0:
                        check = 1
                        break
                if check == 1:
                    continue
                if j+k == N-1:
                    if j == 0:
                        count += 1
                    else:
                        if puzzle[i][j-1] == 0:
                            count += 1
                else:
                    if puzzle[i][j+k+1] == 0:
                        if j == 0:
                            count += 1
                        else:
                            if puzzle[i][j-1] == 0:
                                count += 1
    print(count)

    count2 = 0

    for i in range(N-K+1):

        for j in range(N):
            check2 = 0
            # if check2 == 1:
            #     break
            if puzzle[i][j] == 1:
                # if check2 == 1:
                #     break
                for k in range(K):
                    if puzzle[i+k][j] == 0:
                        check2 = 1
                        break
                if check2 == 1:
                    continue
                if i+k == N-1:
                    if i == 0:
                        count2 += 1
                    else:
                        if puzzle[i-1][j] == 0:
                            count2 += 1
                else:
                    if puzzle[i+k+1][j] == 0:
                        if i == 0:
                            count2 += 1
                        else:
                            if puzzle[i-1][j] == 0:
                                count2 += 1
    print(count2)

    print("#{} {}".format(tc, count+count2))