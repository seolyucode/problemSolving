# 1267. [S/W 문제해결 응용] 10일차 - 작업순서

import sys
sys.stdin = open('input.txt', 'r')

# def display(arr):
#     for i in range(len(arr)):
#         for j in range(len(arr[i])):
#             print(arr[i][j], end=' ')
#         print()
#     print()
#
# for tc in range(3):
#     V, E = map(int, input().split())
#     temp = list(map(int, input().split()))
#     board = []
#
#     for i in range(V + 1):
#         t = []
#         for j in range(V + 1):
#             t.append(0)
#         board.append(t)
#
#     for i in range(E):
#         board[temp[2 * i]][temp[2 * i + 1]] = 1
#
#     display(board)

for tc in range(3):
    V, E = map(int, input().split())
    E_lst = list(map(int, input().split()))
    print(E_lst)
    lst = [[] for _ in range(V+1)]
    for i in range(len(E_lst)//2):
        lst[E_lst[2*i]].append(E_lst[2*i+1])
        # lst[E_lst[2*i+1]].append(E_lst[2*i])

    print(lst)