# 2063. 중간값 찾기

N = int(input())
lst = input().split()
numbers = list(sorted(map(int, lst)))
center = int(N//2)
print(numbers[center])