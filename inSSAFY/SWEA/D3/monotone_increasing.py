# 6190. 정곤이의 단조 증가하는 수

def monotone_increasing(x):
    str_N = str(x)
    for i in range(len(str_N)-1):
        if str_N[i] > str_N[i+1]:
            return False
    return True

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    N_lst = list(map(int, input().split()))

    lst = []
    for i in range(0, N-1):
        for j in range(i+1, N):
            lst.append(N_lst[i]*N_lst[j])

    lst_mi = []
    for i in lst:
        if monotone_increasing(i):
            lst_mi.append(i)

    if not lst_mi:
        print("#{} {}".format(tc, -1))
    else:
        print("#{} {}".format(tc, max(lst_mi)))