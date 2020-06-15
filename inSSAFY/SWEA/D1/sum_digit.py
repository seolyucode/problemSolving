# 2058. 자릿수 더하기

N = int(input())
sum = 0
for i in range(4):
    a = N % 10
    N = N // 10
    sum += a
print (sum)