# [S/W 문제해결 기본] 3일차 - 회문2

# import sys
# sys.stdin = open("input2.txt", 'r')

for tc in range(1, 11):
    n = int(input())
    letter_board = [input() for i in range(100)]
    letter_board_rotation = list(zip(*letter_board))

    lst1 = []
    for k in range(1, 101):
        for i in range(len(letter_board)):
            for j in range(100-k+1):
                if letter_board[i][j:j+k] == letter_board[i][j:j+k][::-1]:
                    lst1.append(letter_board[i][j:j+k])

        for i in range(len(letter_board_rotation)):
            for j in range(100-k+1):
                if letter_board_rotation[i][j:j+k] == letter_board_rotation[i][j:j+k][::-1]:
                    lst1.append(''.join(letter_board_rotation[i][j:j+k]))

    print('#', tc, sep='', end=' ')

    lst2 = []
    for i in range(len(lst1)):
        lst2.append(len(lst1[i]))

    print(max(lst2))