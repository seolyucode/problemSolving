# DFS와 BFS

# 인접 리스트

n, m, start = map(int, input().split())  # n: 정점의 개수 / m: 간선의 개수 / v: 탐색 시작 정점
a = [[] for _ in range(n+1)]
check = [False] * (n+1)

for _ in range(m):
    u, v = map(int, input().split())
    a[u].append(v)
    a[v].append(u)

for i in range(n+1):
    a[i].sort()

def dfs(x):
    global check
    check[x] = True
    print(x, end=' ')
    for y in a[x]:
        if check[y] == False:
            dfs(y)

def bfs(start):
    check = [False] * (n + 1)
    queue = []
    queue.append(start)
    check[start] = True
    while queue:
        x = queue.pop(0)
        print(x, end=' ')
        for y in a[x]:
            if not check[y]:
                check[y] = True
                queue.append(y)

dfs(start)
print()
bfs(start)
print()