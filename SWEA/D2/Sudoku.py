# 1974. 스도쿠 검증

T = int(input())

for tc in range(1, T+1):

    sudoku = [list(map(int, input().split())) for _ in range(9)]
    print(sudoku)

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

    print(sum_list1)
    print(sum_list2)
