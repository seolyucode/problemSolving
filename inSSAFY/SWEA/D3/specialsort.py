# 4843. [파이썬 S/W 문제해결 기본] 2일차 - 특별한 정렬

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = sorted(list(map(int, input().split())))

    lst = []
    lst.append(numbers[-1])
    lst.append(numbers[0])
    lst.append(numbers[-2])
    lst.append(numbers[1])
    lst.append(numbers[-3])
    lst.append(numbers[2])
    lst.append(numbers[-4])
    lst.append(numbers[3])
    lst.append(numbers[-5])
    lst.append(numbers[4])
    
    print('#', tc, sep='', end=' ')
    print(' '.join(map(str, lst)))