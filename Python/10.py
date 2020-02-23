'''
함수 만들기

def add(a, b):
    c=a+b
    print(c)

add(3, 2)
add(5, 7)

def add(a, b):
    c=a+b
    return c

print(add(3, 2))

x=add(3, 2)
print(x)
'''

# 튜플로 여러개의 값을 리턴
def add(a, b):
    c=a+b
    d=a-b
    return c, d

print(add(3, 2))


a=[12, 13, 7, 9, 19]

def isPrime(x):
    for i in range(2, x):
        if x%i==0:
            return False
    return True

for y in a:
    if isPrime(y):
        print(y, end=' ')