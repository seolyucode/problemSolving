# [S/W 문제해결 기본] 1일차 - View

for tc in range(1, 11):
    N = int(input())
    H = list(map(int, input().split()))
 
    sum = 0
    for i in range(2, N-2):
        if H[i] >= max(H[i-1], H[i-2], H[i+1], H[i+2]):
            num = H[i] - max(H[i-1], H[i-2], H[i+1], H[i+2])
            sum += num
    print("#%d %d" % (tc, sum))