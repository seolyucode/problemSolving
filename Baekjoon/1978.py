# 소수 찾기

def is_prime(x):
    if x < 2:
        return False
    elif x==2:
        return True
    else:
        for i in range(2, x):
            if x%i==0:
                return False
        return True

N = int(input())
lst = list(map(int, input().split()))

lst_prime = []
for i in lst:
    lst_prime.append(is_prime(i))

print(lst_prime.count(True))

'''
def is_prime(x):
    if x < 2:
        return False
    i = 2
    while i*i <= x:
        if x % i == 0:
            return False
        i += 1
    return True

n = int(input())
a = list(map(int,input().split()))
ans = 0
for x in a:
    if is_prime(x):
        ans += 1
print(ans)
'''