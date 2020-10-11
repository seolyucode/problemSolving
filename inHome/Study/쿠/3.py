def solution(k, score):
    lst = []
    for i in range(len(score) - 1):
        lst.append(score[i] - score[i + 1])
    check = []
    for i in lst:
        if (lst.count(i) >= k):
            continue
        else:
            check.append(i)
    # 예외처리해야함
    return len(check)-1

print(solution(3, [24, 22, 20, 10, 5, 3, 2, 1]))
print(solution(2, [1300000000,700000000,668239490,618239490,568239490,568239486,518239486,157658638,157658634,100000000,100]))
print(solution(3, [24, 23, 22, 21, 20, 19, 18, 17]))