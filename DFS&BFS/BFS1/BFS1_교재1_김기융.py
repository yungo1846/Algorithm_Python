# 음료수 얼려 먹기
N, M = list(map(int, input().split()))

ice = []
for i in range(N):
    ice.append(list(map(int, input())))

visited = [[False for _ in range(M)] for _ in range(N)]


def dfs(x, y):
    global visited
    visited[x][y] = True
    if x < N - 1 and ice[x + 1][y] == 0 and not visited[x + 1][y]:
        dfs(x+1, y)
    if x > 0 and ice[x - 1][y] == 0 and not visited[x-1][y]:
        dfs(x - 1, y)
    if y < M - 1 and ice[x][y + 1] == 0 and not visited[x][y + 1]:
        dfs(x, y+1)
    if y > 0 and ice[x][y-1] == 0 and not visited[x][y-1]:
        dfs(x, y - 1)


count = 0
for i in range(N):
    for j in range(M):
        if visited[i][j] == False and ice[i][j] == 0:
            print(i, j)
            count += 1
            dfs(i, j)
            print(visited)

print(count)
