from collections import deque

N, M = list(map(int, input().split()))

miro = []
for i in range(N):
    miro.append(list(map(int, input())))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if miro[nx][ny] == 0:
                continue

            if miro[nx][ny] == 1:
                queue.append((nx, ny))
                miro[nx][ny] = miro[x][y] + 1
    return miro[N - 1][M - 1]


print(bfs(0, 0))
