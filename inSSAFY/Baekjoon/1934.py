# 최소공배수

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)

T = int(input())

for tc in range(1, T+1):
    N1, N2 = map(int, input().split())

    print(N1*N2//gcd(N1, N2))