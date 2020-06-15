# [S/W 문제해결 기본] 1일차 - Flatten

for tc in range(1, 11):
    N = int(input())
    lst = sorted(list(map(int, input().split())))

    for i in range(N):
        lst[-1] -= 1
        lst[0] += 1
        lst.sort()

    print("#", tc, sep='', end=' ')
    print(max(lst)-min(lst))
