import sys
sys.stdin = open('input.txt', 'r')

# 1번 벽
def fisrt_m(ant, board):
    if current == 0:
        return 3
    elif current == 1:
        return 2
    elif current == 2:
        return 1
    else:
        return 0

# 2번 벽
def second_m(ant, board):
    if current == 0:
        return 2
    elif current == 1:
        return 3
    elif current == 2:
        return 0
    else:
        return 1

def is_wall(ant, board):
    return ant[0] < 0 or ant [1] < 0 or ant[0] >= len(board) or ant[1] >= len(board)

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for i in range(N)]

    ant = [0, 0]
    count = 0

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    # 현재 위치
    current = 0

     while 1:

        ant[0] += dx[current]
        ant[1] += dy[current]

        if is_wall(ant, board):
            break

        if board[ant[0]][ant[1]] == 1:
            current = fisrt_m(ant, board)

        if board[ant[0]][ant[1]] == 2:
            current = second_m(ant, board)

        count += 1

    print("#{} {}".format(tc, count))