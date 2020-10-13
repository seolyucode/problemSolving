from collections import deque

def isWall(x, y, n, m):
    if x < 0 or x > n - 1 or y < 0 or y > m - 1:
        return True
    return False

def solution(n, m, array):
    visited = [[0] * m for _ in range(n)]
    answer = 0 
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    queue = deque()
    queue.append((0, 0, 1)) # 시작지점 걸음 수 
    visited[0][0] = 1
    while True:
        # print("==========================")
        # for line in visited:
        #     print(line)
        # print("==========================")
        x, y, count = queue.popleft() # (0, 0, 1)
        if (x == n - 1 and y == m - 1):
            return count 
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if isWall(xx, yy, n, m):
                continue
            if array[xx][yy] == 0:
                continue
            if visited[xx][yy] == 1:
                continue
           
            visited[xx][yy] = 1
            queue.append((xx, yy, count + 1))
            # if (isWall(xx, yy, n, m)==False) and array[xx][yy] == 1:
            #     x = xx
            #     y = yy
            #     answer += 1
            #     break
            # else:
            #     continue


    return answer

print(solution(5, 6, [[1, 0, 1, 0, 1, 0], [1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]))