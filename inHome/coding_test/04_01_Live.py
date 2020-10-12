def isWall(x, y, n):
    if x < 0 or x > n - 1 or y < 0 or y > n - 1:
        return True
    return False
def solution(n, plans):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    direction = ['U', 'R', 'D', 'L']
    x = 0
    y = 0
    for plan in plans:
        mode = direction.index(plan)  # 1 1 1 0 2 2
        # print(mode)
        xx = x + dx[mode]
        yy = y + dy[mode]
        result = isWall(xx, yy, n)
        if result:
            continue
        x = xx
        y = yy
    return x+1, y+1





print(solution(5, ['R','R','R','U','D','D']))