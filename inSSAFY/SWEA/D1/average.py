# 2071. 평균값 구하기

T = int(input())
for i in range(T):
    lst = input().split()
    numbers = list(map(int, lst))
    print('#', i+1, sep="", end=" ")
    print(round(sum(numbers)/len(numbers)))