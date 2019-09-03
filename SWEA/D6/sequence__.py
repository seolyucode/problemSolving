import sys
sys.stdin = open('input.txt', 'r')

# def display(arr):
#     for i in range(len(arr)):
#         for j in range(len(arr[i])):
#             print(arr[i][j], end=' ')
#         print()
#     print()

for tc in range(3):
    V, E = map(int, input().split())
    temp = list(map(int, input().split()))
    board = []

    for i in range(V + 1):
        t = []
        for j in range(V + 1):
            t.append(0)
        board.append(t)

    for i in range(E):
        board[temp[2 * i]][temp[2 * i + 1]] = 1

