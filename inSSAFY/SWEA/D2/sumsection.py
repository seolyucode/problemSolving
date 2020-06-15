# 4835. [파이썬 S/W 문제해결 기본] 1일차 - 구간합

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    sum_lst = []
    sum_lst2 = []
    sum_lst3 = []
    for i in range(0, len(lst) - M + 1):
        for j in range(i, i + M):
            sum_lst2.append(lst[j])
        sum_lst3.append(sum(sum_lst2))
        sum_lst2 = []

    print('#', tc, sep='', end=' ')
    print(max(sum_lst3)-min(sum_lst3))

# 하나 빼고 하나 더하는 방식으로 하기



