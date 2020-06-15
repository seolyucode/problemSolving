# [S/W 문제해결 기본] 3일차 - 회문1

import sys
sys.stdin = open("input.txt", "r")

for tc in range(1, 11):
    n = int(input())
    letter_board = [input() for i in range(8)]

    count1 = 0
    for i in range(len(letter_board)):
        for j in range(8-n+1):
            if letter_board[i][j:j+n] == letter_board[i][j:j+n][::-1]:
                count1 += 1

    letter_board_rotation = list(zip(*letter_board))

    count2 = 0
    for i in range(len(letter_board_rotation)):
        for j in range(8-n+1):
            if letter_board_rotation[i][j:j+n] == letter_board_rotation[i][j:j+n][::-1]:
                count2 += 1

    print('#', tc, sep='', end=' ')
    print(count1 + count2)