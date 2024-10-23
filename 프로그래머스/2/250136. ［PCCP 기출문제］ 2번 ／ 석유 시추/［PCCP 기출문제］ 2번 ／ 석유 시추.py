# bfs
from collections import deque
def solution(land):
    n,m = len(land), len(land[0])
    visit = [[0] * m for _ in range(n)]
    answer = [0] * m
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    def bfs(i,j):
        queue = deque([(i,j)])
        min_y, max_y = m,0
        size = 0
        while queue:
            x,y = queue.popleft()
            if visit[x][y] == 0:
                size += 1
                min_y = min(min_y,y)
                max_y = max(max_y,y)
                visit[x][y] = 1
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < m:
                        if land[nx][ny] == 1 and visit[nx][ny] == 0:
                            queue.append((nx,ny))
                            
        for i in range(min_y,max_y+1):
            answer[i] += size
                            
    
    for i in range(n):
        for j in range(m):
            if visit[i][j] == 0 and land[i][j] == 1:
                bfs(i,j)
    
    return max(answer)