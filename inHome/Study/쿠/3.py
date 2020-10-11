def solution(k, score):
    # lst = []
    # for i in range(len(score) - 1):
    #     lst.append(score[i] - score[i + 1])
    # check = []
    # for i in lst:
    #     if (lst.count(i) >= k):
    #         continue
    #     else:
    #         check.append(i)

    # 예외처리해야함
    # 시간복잡도 줄이기
    # return len(check)-1

    scoreDiffList = []
    scoreDiffDic = {}
    checkList = []
    for i in range(len(score) - 1):
        diff_score = score[i] - score[i + 1]
        scoreDiffList.append(diff_score)
        if scoreDiffDic.get(diff_score):
            scoreDiffDic[diff_score] += 1
        else:
            scoreDiffDic[diff_score] = 1
    for scoreDiff in scoreDiffList:
        if scoreDiffDic[scoreDiff] < k:
            checkList.append(scoreDiff)
    if len(checkList) > 0:
        return len(checkList) - 1
    return len(checkList)
    
print(solution(3, [24, 22, 20, 10, 5, 3, 2, 1]))
print(solution(2, [1300000000,700000000,668239490,618239490,568239490,568239486,518239486,157658638,157658634,100000000,100]))
print(solution(3, [24, 23, 22, 21, 20, 19, 18, 17]))