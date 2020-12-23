# 구슬탈출 2
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 1. 빨간 구슬과 파란 구슬을 기울인 방향에 대해서 갈 수 있는 만큼 이동했을 때의 좌표를 구한다

# 2. 중간에 파란 구슬이 구멍에 빠지면 continue하여 다른 방향으로 기울인 경우로 넘어간다

# 3. 빨간 구슬과 파란 구슬이 겹치면 각각 이동한 길이를 구하여 앞뒤로 위치하도록 처리한다

# 4. 빨간 구슬이 빠지면 기울인 횟수를 출력하고 10번이 넘어가면 -1 출력


def bfs(rx, ry, bx, by, cnt):
    q.append([rx, ry, bx, by])
    c.append([rx, ry, bx, by])  # c는 여기서 visited 같은 역할
    while q:
        qlen = len(q)
        while qlen:
            rx, ry, bx, by = q.popleft()
            if a[rx][ry] == 'O':
                print(cnt)
                return
            for i in range(4):
                nrx, nry, nbx, nby = rx, ry, bx, by
                while True:  # 벽까지 계속 이동
                    nrx += dx[i]
                    nry += dy[i]
                    if a[nrx][nry] == 'O':
                        break
                    if a[nrx][nry] == '#':
                        nrx -= dx[i]
                        nry -= dy[i]
                        break
                while True:
                    nbx += dx[i]
                    nby += dy[i]
                    if a[nbx][nby] == 'O':
                        break
                    if a[nbx][nby] == '#':
                        nbx -= dx[i]
                        nby -= dy[i]
                        break

                if a[nbx][nby] == 'O':  # 파란색이 구멍에 들어간 경우 실패, 계속 진행
                    continue
                if nrx == nbx and nry == nby:  # 빨간, 파란 공의 위치가 같은 경우 더 많이 이동한 거리에 따라 위치 재조정
                    if abs(rx - nrx) + abs(ry - nry) > abs(bx - nbx) + abs(by - nby):
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]

                if [nrx, nry, nbx, nby] not in c:
                    c.append([nrx, nry, nbx, nby])
                    q.append([nrx, nry, nbx, nby])
            qlen -= 1

        if cnt == 10:
            print(-1)
            return
        cnt += 1
    print(-1)
    return


n, m = map(int, input().split())
a = [[] for _ in range(n)]
c, q, cnt = [], deque(), 0

for i in range(n):
    a[i] = list(map(str, input()))
    for j in range(m):
        if a[i][j] == 'R':
            rx, ry = i, j
        elif a[i][j] == 'B':
            bx, by = i, j

bfs(rx, ry, bx, by, cnt)
