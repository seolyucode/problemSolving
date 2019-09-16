# 5186. [파이썬 S/W 문제해결 구현] 1일차 - 이진수2

def decpo(n):
    result = ''
    cnt = 0

    while 1:
        if n == 0.0:
            return result
        elif cnt >= 13:
            return 'overflow'

        n = n * 2
        intnum = int(n)
        result += str(intnum)
        n = n - intnum
        cnt += 1

t = int(input())

for tc in range(1, t+1):
    number = float(input())
    print("#{} {}".format(tc, decpo(number)))