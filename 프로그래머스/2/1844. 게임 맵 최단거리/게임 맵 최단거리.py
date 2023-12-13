from collections import deque
def solution(maps):
    answer = 0
    x_len = len(maps[0])
    y_len = len(maps)
    visited = [[0]*x_len for _ in range(y_len)]
    x_map = [-1,1,0,0]
    y_map = [0,0,1,-1]
    que = deque()
    que.append((0,0))
    visited[0][0] = 1    
    while que:
        y,x = que.popleft()
        for i in range(4):
            dx = x + x_map[i]
            dy = y + y_map[i]
            if dx < 0 or dx >= x_len or dy < 0 or dy >= y_len:
                continue
            if visited[dy][dx] == 0 and maps[dy][dx] == 1:
                que.append((dy,dx))
                visited[dy][dx] = visited[y][x] + 1
    return visited[y_len-1][x_len-1] if visited[y_len-1][x_len-1] != 0 else -1
