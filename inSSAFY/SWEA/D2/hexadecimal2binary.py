# 5185. [파이썬 S/W 문제해결 구현] 1일차 - 이진수

hexa = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9,
        'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}

def binary(n):
    quo, rem = 0, 0
    result = ''
    for i in range(4):
        quo = n // 2
        rem = n % 2
        result = str(rem) + result
        n = quo
    return result

t = int(input())

for tc in range(1, t+1):
    n, number = list(input().split())

    lst = []
    for i in number:
        lst.append(hexa[i])

    lst2 = []
    for i in lst:
        lst2.append(binary(i))

    print("#{} {}".format(tc, ''.join(lst2)))