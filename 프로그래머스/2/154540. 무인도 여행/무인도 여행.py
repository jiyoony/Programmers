import sys
sys.setrecursionlimit(10000)
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def dfs(x,y,visited,maps):
    stays = 0
    if x >= len(maps) or x < 0 or y < 0 or y >= len(maps[0]):
        return stays
    if visited[x][y] == 0 and maps[x][y] != 'X':   
        visited[x][y] = 1
        for i in range(4):
            stays += dfs(x+dx[i],y+dy[i],visited,maps)
        return int(maps[x][y])+stays
        return 0
    return stays

def solution(maps):
    answer = []
    visited = [[0 for i in range(len(maps[0]))] for j in range(len(maps))]
    new_maps = [list(i) for i in maps]
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            print
            if maps[i][j] != 'X' and visited[i][j] == 0:
                answer.append(dfs(i,j,visited,maps))
    if len(answer) == 0:
        return [-1]
    return sorted(answer)