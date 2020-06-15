# 4837. [파이썬 S/W 문제해결 기본] 2일차 - 부분집합의 합

T = int(input())
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
n = len(arr)

lst = []
for i in range(1<<n):
    subset = []
    for j in range(n):
        if i & (1<<j):
            subset.append(arr[j])
    lst.append(subset)

for tc in range(1, T+1):
    N, K = map(int, input().split())

    len_subset = []
    for i in lst:
        if len(i) == N:
            len_subset.append(i)

    sum_subset = 0
    for i in len_subset:
        if sum(i) == K:
            sum_subset += 1

    print('#%s %d' % (tc, sum_subset))