# 5356. 의석이의 세로로 말해요

T = int(input())

for tc in range(1, T+1):
    words = [input() for _ in range(5)]

    lst = []
    for i in words:
        lst.append(len(i))
    N = max(lst)

    for i in range(5):
        if len(words[i]) < N:
            words[i] += '$'*(N-len(words[i]))

    print("#{}".format(tc), end=' ')

    for j in range(N):
        for i in range(5):
            print(words[i][j].replace('$', ''), end='')
    print()