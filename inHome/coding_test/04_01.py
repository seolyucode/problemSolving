def solution(n, plans):
    # 인덱스[0, 0]
    start = [0, 0]
    
    for plan in plans:
        if plan == 'R':
            if start[1] < n-1:
                start[1] += 1
        elif plan == 'L':
            if start[1] > 0:
                start[1] -= 1
        elif plan == 'U':
            if start[0] > 0:
                start[0] -= 1
        elif plan == 'D':
            if start[0] < n-1:
                start[0] += 1
    
    return ' '.join(str(start[0]+1) + str(start[1]+1))

print(solution(5, ['R','R','R','U','D','D']))