# 1974. 스도쿠 검증

import sys
sys.stdin = open('Sudoku_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):

    sudoku = [list(map(int, input().split())) for _ in range(9)]

    sum_list1 = []
    for i in range(0, 7, 3):
        for j in range(0, 7, 3):
            sum = 0
            for a in range(3):
                for b in range(3):
                    sum += sudoku[i+a][j+b]
            sum_list1.append(sum)

    sum_list2 = []
    for i in sudoku:
        sum = 0
        for j in i:
            sum += j
        sum_list2.append(sum)

    sum_list3 = []
    for j in range(9):
        sum = 0
        for i in range(9):
            sum += sudoku[i][j]
        sum_list3.append(sum)

    sum_list = sum_list1 + sum_list2 + sum_list3

    check = 1
    for i in sum_list:
        if i != 45:
            check = 0

    if check == 1:
        print("#{} {}".format(tc, 1))
    else:
        print("#{} {}".format(tc, 0))