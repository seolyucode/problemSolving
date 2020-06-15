# 5176. [파이썬 S/W 문제해결 기본] 8일차 - 이진탐색

import sys
sys.stdin = open('input3.txt','r')

def inorder_traverse(t):
    global value
    if t <= n:
        inorder_traverse(t*2)
        tree[t] = value
        value += 1
        inorder_traverse(t*2+1)

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    value = 1
    tree = [0] * (n+1)

    inorder_traverse(1)
    print("#{} {} {}".format(tc, tree[1], tree[n//2]))