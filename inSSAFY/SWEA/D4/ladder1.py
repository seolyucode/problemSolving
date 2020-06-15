# 1210. [S/W 문제해결 기본] 2일차 - Ladder1

# import sys
# sys.stdin = open("input.txt", 'r')

for tc in range(1, 11):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(100)]

    icecream = board[99].index(2)

    for i in range(99, 0, -1):
        if icecream == 99:
            while(icecream > 0 and board[i][icecream-1] == 1):
                icecream -= 1
        elif icecream == 0:
            while(icecream < 99 and board[i][icecream+1] == 1):
                icecream += 1
        else:
            if board[i][icecream+1] == 1:
                while icecream < 99 and board[i][icecream+1] == 1:
                    icecream += 1
            elif board[i][icecream-1] == 1:
                while icecream > 0 and board[i][icecream-1] == 1:
                    icecream -= 1

    print(icecream)

