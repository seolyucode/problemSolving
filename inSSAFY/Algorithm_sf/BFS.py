# BFS

# 1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7

lst = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]

adjacency_lst = [[] for _ in range(len(lst)//2)]
for i in range(len(lst)//2):
    adjacency_lst[lst[2*i]].append(lst[2*i+1])
    adjacency_lst[lst[2*i+1]].append(lst[2*i])
print(adjacency_lst)

# lst2 = [[], [2, 3], [1, 4, 5], [1, 7], [2, 6], [2, 6], [4, 5, 7], [3, 6]]

visited = [False] * (8)

def bfs(v):
    q = []
    q.append(v)
    while q:
        v = q.pop(0)
        if not visited[v]:
            visited[v] = 1
            print(v, end=' ')
            for w in adjacency_lst[v]:
                if not visited[w]:
                    q.append(w)

bfs(1)