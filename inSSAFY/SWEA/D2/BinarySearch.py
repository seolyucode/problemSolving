# 4839. [파이썬 S/W 문제해결 기본] 2일차 - 이진탐색

T = int(input())

for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    left = 1
    right = P
    aleft = left
    aright = right
    Acount = 0
    while aleft <= aright:
        center = int((aleft+aright)/2)
        if center == A:
            Acount += 1
            aresult = Acount
            break
        elif center > A:
            aright = center
            Acount += 1
        else:
            aleft = center
            Acount += 1
    bleft = left
    bright = right
    Bcount = 0
    while bleft <= bright:
        center = int((bleft+bright)/2)
        if center == B:
            Bcount += 1
            bresult = Bcount
            break
        elif center > B:
            bright = center
            Bcount += 1
        else:
            bleft = center
            Bcount += 1
    if aresult == bresult:
        result = 0
    elif aresult < bresult:
        result = 'A'
    else:
        result = 'B'
    print('#', tc, sep='', end=' ')
    print(result)
        