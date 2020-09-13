def solution(boxes):
    lst = []
    for i in range(len(boxes)):
        for j in range(2):
            if len(lst) == 0:
                lst.append(boxes[i][j])
            else:
                for k in range(len(lst)):
                    if boxes[i][j] == lst[k]:
                        lst[k] = 0
                        boxes[i][j] = 0
                else:
                    lst.append(boxes[i][j])
    cnt = 0
    for i in lst:
        if i != 0:
            cnt += 1
    return cnt//2

print(solution([[1, 2], [2, 1], [3, 3], [4, 5], [5, 6], [7, 8]]))
print(solution([[1, 2], [3, 4], [5, 6]]))
print(solution([[1, 2], [2, 3], [3, 1]]))