# 1267. [S/W 문제해결 응용] 10일차 - 작업순서

import sys
sys.stdin = open('input.txt', 'r')

for tc in range(10):
    V, E = map(int, input().split())
    E_lst = list(map(int, input().split()))
    started_stack = list(range(1, V+1))
    path = []

    lst = [[] for _ in range(V+1)]
    for i in range(len(E_lst)//2):
        lst[E_lst[2*i]].append(E_lst[2*i+1])
        if E_lst[2*i+1] in started_stack:
            started_stack.remove(E_lst[2*i+1])

    while started_stack:
        current = started_stack.pop()
        next_list = lst[current]
        lst[current] = []

        for next_num in next_list:
            for l in lst:
                if next_num in l:
                    break
            else:
                started_stack.append(next_num)

        path.append(current)

    print('#{} {}'.format(tc+1, ' '.join(list(map(str, path)))))