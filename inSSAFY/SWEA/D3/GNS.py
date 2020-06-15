# [S/W 문제해결 기본] 5일차 - GNS

# import sys
# sys.stdin = open("GNS_test_input.txt", 'r')

sdict = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4,
         "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}

T = int(input())
for tc in range(1, T+1):
    tc_num, n = input().split()
    s = list(input().split())

    for i in range(len(s)-1, 0, -1):
        for j in range(i):
            if sdict[s[j]] > sdict[s[j+1]]:
                s[j], s[j+1] = s[j+1], s[j]

    print('#', tc, sep='')
    print(' '.join(s))