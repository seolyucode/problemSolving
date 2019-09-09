# 1231. [S/W 문제해결 기본] 9일차 - 중위순회

import sys
sys.stdin = open('Inorder_Traversal_input.txt', 'r')

def inorder_traverse(T):
    if T:
        inorder_traverse(tree[T][0])
        print(tree[T][2], end = '')
        inorder_traverse(tree[T][1])

def is_edge(x, n):
    if x < n:
        return True

dx = [1, 2]

for tc in range(1, 11):
    V = int(input())
    tree = [[0] * 3 for _ in range(V+1)]

    node_info = [list(input().split()) for _ in range(V)]

    for i in node_info:

        parent = int(i[0])
        x = 1
        X1 = x + dx[0]
        X2 = x + dx[1]

        if is_edge(X1, len(i)):
            tree[parent][0] = int(i[2])
        if is_edge(X2, len(i)):
            tree[parent][1] = int(i[3])

        tree[parent][2] = i[1]

    print("#{}".format(tc), end = ' ')
    inorder_traverse(1)
    print()