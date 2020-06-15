# 4871. [파이썬 S/W 문제해결 기본] 4일차 - 그래프 경로

# def dfs(x):
#     global check
#     global path
#     check[x] = True
#     path.append(x)
#     for y in node_lst[x]:
#         if check[y] == False:
#             dfs(y)
#     return path

import sys
sys.stdin = open('GraphPath_input.txt', 'r')

def dfs(x):
    global check
    global path
    stack = []
    stack.append(x)
    while True:
        if stack == []:
            return path
        x = stack.pop()
        if check[x] == False:
            for i in node_lst[x]:
                stack.append(i)
            check[x] = True
            path.append(x)

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    node_lst = [[] for _ in range(V+1)]

    for i in range(E):
        s, e = map(int, input().split())
        node_lst[s].append(e)

    S, G = map(int, input().split())

    check = [False] * (V+1)
    path = []

    G_path = dfs(S)

    if G in G_path:
        print("#{} {}".format(tc, 1))
    else:
        print("#{} {}".format(tc, 0))