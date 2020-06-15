# 6485. 삼성시의 버스 노선

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    Bus_station = [0]*5001
    for i in range(N):
        A, B = map(int, input().split())
        for bus in range(A, B+1):
            Bus_station[bus] += 1
    P = int(input())
    lst = []
    for i in range(P):
        C = int(input())
        lst.append(Bus_station[C])

    print(lst)
    res = list(map(str, lst))
    print(res)
    print("#{} {}".format(tc, ' '.join(res)))