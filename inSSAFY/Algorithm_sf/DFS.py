# DFS

# 1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7

lst = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]

lst2 = [[] for _ in range(8)]
for i in range(len(lst)//2):
    lst2[lst[2*i]].append(lst[2*i+1])
    lst2[lst[2*i+1]].append(lst[2*i])
print(lst2)

# lst2 = [[], [2, 3], [1, 4, 5], [1, 7], [2, 6], [2, 6], [4, 5, 7], [3, 6]]

# 재귀 구현
check = [False] * (8)

def dfs(x):
    global check
    check[x] = True
    print(x, end=' ')
    for y in lst2[x]:
        if check[y] == False:
            dfs(y)

dfs(1)
print()

visited = [False] * (8)
visited[0] = True
def DFS(x):
    global visited
    stack = []
    stack.append(x)
    result = ''
    while True:
        print(stack)
        if stack == []:
            return result
        x = stack.pop()  # pop(0) : BFS
        if visited[x] == False:
            for i in lst2[x]:
                stack.append(i)
                visited[x] = True
            result += str(x) + ' '

print(DFS(1))