# 2068. 최대수 구하기

T = int(input())
for i in range(T):
    n = input().split()
    numbers = list(sorted(map(int, n)))
    print('#', i+1, sep='', end=' ')
    print(numbers[-1])