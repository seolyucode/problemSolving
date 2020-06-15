def preorder_traverse(T):
    if T:
        print("%d" %T, end=' ')
        preorder_traverse(tree[T][0])
        preorder_traverse(tree[T][1])

V = int(input())
tree = [[0] * 2 for _ in range(V+1)]

Edge_list = list(map(int, input().split()))

for i in range(len(Edge_list) // 2):
    parent, child = Edge_list[i*2], Edge_list[i*2+1]
    if not tree[parent][0]:
        tree[parent][0] = child
    else:
        tree[parent][1] = child

print(tree)
preorder_traverse(1)
print()


# test = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13 // 24 12