# 4828. [파이썬 S/W 문제해결 기본] 1일차 - min max

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    largest = lst[0]
    for i in lst:
        if i > largest:
            largest = i
    smallest = lst[0]
    for j in lst:
        if j < smallest:
            smallest = i
    print('#', tc, sep="", end=" ")
    print(largest - smallest)