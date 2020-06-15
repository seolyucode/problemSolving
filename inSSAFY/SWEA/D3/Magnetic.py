# [S/W 문제해결 기본] 5일차 - Magnetic

# import sys
# sys.stdin = open("input3.txt", 'r')

for tc in range(1, 11):
    side = int(input())
    table = [list(map(int, input().split())) for i in range(side)]

    count = 0
    for i in range(side):
        for j in range(side):
            if table[i][j] == 1:
                for k in range(i+1, side):
                    if table[k][j] == 1:
                        break
                    elif table[k][j] == 2:
                        count += 1
                        break

    print("#{} {}".format(tc, count))

