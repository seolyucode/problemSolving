# 4834. [파이썬 S/W 문제해결 기본] 1일차 - 숫자 카드

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input()))

    largest=0
    for i in lst:
        if lst.count(i) > largest:
            largest = lst.count(i)

    lst2 = []
    for j in lst:
        if lst.count(j)==largest:
            lst2.append(j)

    print('#', tc, sep='', end=' ')
    print(max(lst2), largest)
