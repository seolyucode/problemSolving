def solution(N):
    maxNum = 0
    result = 0
    Number = N
    for i in range(2, 10):
        N = Number
        lst = []
        while (N):
            lst.append(N % i)
            N = int(N / i)
        lst2 = []
        for j in lst:
            if j == 0:
                continue
            else:
                lst2.append(j)
        result2 = 1
        for j in lst2:
            result2 *= j
        if result2 >= result:
            result = result2
            maxNum = i
    answer = []
    answer.append(maxNum)
    answer.append(result) 
    
    return answer


print(solution(10))
print(solution(14))