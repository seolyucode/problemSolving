# 1267. [S/W 문제해결 응용] 10일차 - 작업순서

import sys
sys.stdin = open('input.txt', 'r')

# def display(arr):
#     for i in range(len(arr)):
#         for j in range(len(arr[i])):
#             print(arr[i][j], end=' ')
#         print()
#     print()
#
# for tc in range(3):
#     V, E = map(int, input().split())
#     temp = list(map(int, input().split()))
#     board = []
#
#     for i in range(V + 1):
#         t = []
#         for j in range(V + 1):
#             t.append(0)
#         board.append(t)
#
#     for i in range(E):
#         board[temp[2 * i]][temp[2 * i + 1]] = 1
#
#     display(board)

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
        # lst[E_lst[2*i+1]].append(E_lst[2*i])

    visited = [False] * (V+1)

    while started_stack:    # stack이 비면 작업을 종료
        current = started_stack.pop()   # 스택의 최근값을 current에 저장하고 삭제
        next_list = lst[current]    # current와 간선으로 연결된 다음 수들을 찾기
        lst[current] = []       # 한번 탐색한 간선은 제거를 위해 빈 리스트로..

        for next_num in next_list:  # 다음 수들에 선행으로 연결된 간선이 없는지 (새로운 시작점이 될 수 있는지) 검사
            for l in lst:
                if next_num in l:   # 연결된 수들의 모임인 lst에 해당 수가 있으면 시작점이 될 수 없음
                    break
            else:           # for문을 다 돌면 선행 연결된 간선이 없는것이므로 시작점이 된다.
                started_stack.append(next_num)

        path.append(current)    # 현재 숫자는 지나온 경로이므로 저장

    print('#{} {}'.format(tc+1, ' '.join(list(map(str, path)))))