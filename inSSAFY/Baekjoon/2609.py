# 최대공약수와 최소공배수
# 최소공배수 = 두 수의 곱/두 수의 최대공약수

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)

def lcm(x, y):
    return (x * y // gcd(x, y))

N1, N2 = map(int, input().split())

print(gcd(N1, N2))
print(lcm(N1, N2))
