# 1238. [S/W 문제해결 기본] 10일차 - Contact

import sys
sys.stdin = open('Contact_input.txt', 'r')

for tc in range(10):
    n, s = map(int, input().split())
    data = list(map(int, input().split()))

    contact = [[] * 101 for _ in range(101)]
    for i in range(len(data)//2):
        contact[data[2*i]].append(data[2*i+1])

    visited = [False] * (101)
    visited[0] = True
    queue = [s]
    path = []

    while queue:
        t = queue.pop(0)
        if visited[t] == False:
            visited[t] = True
            path.append(t)
        for i in contact[t]:
            if visited[i] == False:
                queue.append(i)

    print(path)