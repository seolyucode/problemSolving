# 5174. [파이썬 S/W 문제해결 기본] 8일차 - subtree

def postorder_traverse(T):
    global count
    if T:
        postorder_traverse(tree[T][0])
        postorder_traverse(tree[T][1])
        count += 1

    return count

import sys
sys.stdin = open('subtree_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    e, n = map(int, input().split())

    templ = list(map(int, input().split()))

    tree = [[0]*2 for _ in range(e+2)]

    for i in range(e):
        if tree[templ[2*i]][0] == 0:
            tree[templ[2*i]][0] = templ[2*i+1]
        else:
            tree[templ[2*i]][1] = templ[2*i+1]

    count = 0
    print("#{}".format(tc), end=' ')
    print(postorder_traverse(n))