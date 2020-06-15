# GCD 합

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)

t = int(input())

for tc in range(1, t+1):

    lst = list(map(int, input().split()))
    n = lst[0]
    lst = lst[1:]

    gcd_sum = 0
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            gcd_sum += gcd(lst[i], lst[j])

    print(gcd_sum)