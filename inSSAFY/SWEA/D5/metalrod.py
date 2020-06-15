# 1259. [S/W 문제해결 응용] 7일차 - 금속막대

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    metalnum = list(map(int, input().split()))

    nuts = metalnum[1::2]  # 암나사 크기

    # metals에 각각의 원형 금속 막대를 리스트로 append
    metals = []  
    for i in range(n):
        metals.append([metalnum.pop(0), metalnum.pop(0)])

    # 맞는 암나사가 없는 원형 금속 막대를 result 리스트의 첫번째 값으로 append
    result = []
    for j in range(n):
        if metals[j][0] not in nuts:
            result.append(metals[j])

    # result 리스트에 들어있는 원형 금속 막대가 n개가 될 때까지
    i = 0
    while (len(result) < n):
        for k in range(n):
            if metals[k][0] == result[-1][1]:
                result.append(metals[k])
                break
    
    print ('#', tc, sep='', end=' ')
    
    for l in range(len(result)):
        for m in range(len(result[l])):
            print(result[l][m], end=' ')