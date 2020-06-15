# 직사각형 네개의 합집합의 면적 구하기

plane = [[0 for i in range(100)] for j in range(100)]

for i in range(4):
    start_x, start_y, end_x, end_y = map(int, input().split())

    for x in range(start_x, end_x):
        for y in range(start_y, end_y):
            if plane[x][y] == 0:
                plane[x][y] += 1

sum = 0
for i in range(100):
    for j in range(100):
        if plane[i][j] == 1:
            sum += 1

print(sum)