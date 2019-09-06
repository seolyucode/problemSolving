# 2819. 격자판의 숫자 이어 붙이기
import sys
sys.stdin = open('grating_input.txt', 'r')

def is_wall(x, y):
    return x < 0 or y < 0 or x >= 4 or y >= 4

def find_numbers(grating, x, y, number):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    global result
    if len(number) == 7:
        number = ''.join(list(map(str, number)))
        result.add(number)
    else:
        for vector in directions:
            next_x, next_y = x + vector[0], y + vector[1]
            if is_wall(next_x, next_y):
                continue
            else:
                number.append(grating[next_x][next_y])
                find_numbers(grating, next_x, next_y, number)
                number.pop()

T = int(input())

for tc in range(1, T+1):
    grating = [list(map(int, input().split())) for i in range(4)]
    result = set()

    for i in range(4):
        for j in range(4):
            find_numbers(grating, i, j, [grating[i][j]])
    print(len(result))

