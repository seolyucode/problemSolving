# 4861. [파이썬 S/W 문제해결 기본] 3일차 - 회문

import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    letter_board = [input() for i in range(N)]

    for i in range(len(letter_board)):
        for j in range(N-M+1):
            if letter_board[i][j:j+M] == letter_board[i][j:j+M][::-1]:
                print('#', tc, sep='', end= ' ')
                print(letter_board[i][j:j+M])

    letter_board_rotation = list(zip(*letter_board))

    for i in range(len(letter_board_rotation)):
        for j in range(N-M+1):
            if letter_board_rotation[i][j:j+M] == letter_board_rotation[i][j:j+M][::-1]:
                print('#', tc, sep='', end=' ')
                print(''.join(letter_board_rotation[i][j:j+M]))