# 2072. 홀수만 더하기

T = int(input())
for i in range(T):
    lst = input().split()
    numbers = list(map(int, lst))
    sum = 0
    for j in numbers:
        if j%2==1:
            sum += j
    print('#', i+1, sep="", end=" ")
    print(sum)