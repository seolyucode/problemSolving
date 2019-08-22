# 색종이

plane = [[0 for i in range(101)] for j in range(101)]

N = int(input())

for i in range(N):
    start_x, start_y, w, h = map(int, input().split())
    end_x = start_x + w
    end_y = start_y + h

    for x in range(start_x, end_x):
        for y in range(start_y, end_y):
            plane[x][y] = i+1

for i in range(N):
    count = 0
    for j in range(101):
        for k in range(101):
            if plane[j][k] == i+1:
                count += 1
    print(count)