# 4864. [파이썬 S/W 문제해결 기본] 3일차 - 문자열 비교

def BruteForce(p, t):
    i = 0
    j = 0
    while j < str1_len and i < str2_len:
        if t[i] != p[j]:
            i = i - j
            j = -1
        i = i + 1
        j = j + 1
    if j == str1_len:
        # return i - str1_len
        return 1
    else:
        # return -1
        return 0

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    str1_len = len(str1)
    str2_len = len(str2)

    print('#', tc, sep='', end=' ')
    print(BruteForce(str1, str2))