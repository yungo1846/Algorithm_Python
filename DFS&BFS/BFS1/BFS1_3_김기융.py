# pypy3로 통과
import sys
from collections import deque
m, n, h = list(map(int, input().split()))
graph = [[] for _ in range(h)]
for i in range(h):
    for j in range(n):
        graph[i].append(list(map(int, sys.stdin.readline().rstrip().split())))

# 3차원
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

# 3차원 배열이므로 z, x, y 순으로 입력해야 기존 2차원 배열의 x,y와 같이 동작.


def bfs(z, x, y):
    q = deque()
    q.append((z, x, y))
    while q:
        z, x, y = q.popleft()
        for i in range(6):
            new_x = x + dx[i]
            new_y = y + dy[i]
            new_z = z + dz[i]
            # 배열을 벗어나는지 체크
            if new_x < 0 or new_x >= n or new_y < 0 or new_y >= m or new_z < 0 or new_z >= h:
                continue
            # 탐색하지 않은 노드인지와 만약 탐색된 노드라면 현재 노드의 계산값보다 더 큰지 체크
            # ex
            # 100
            # 000
            # 001 3x3 배열에서 최대값은 2가 돼야하기 때문
            if graph[new_z][new_x][new_y] == 0 or graph[new_z][new_x][new_y] > graph[z][x][y] + 1:
                q.append((new_z, new_x, new_y))
                graph[new_z][new_x][new_y] = graph[z][x][y] + 1
    return graph


# 토마토 익히기
for z in range(h):
    for x in range(n):
        for y in range(m):
            if graph[z][x][y] == 1:
                graph = bfs(z, x, y)

# 토마토가 모두 익었는지와 가장 큰 값이 무엇인지 체크


def check():
    max_count = 0
    for z in range(h):
        for x in range(n):
            for y in range(m):
                if graph[z][x][y] == 0:
                    return - 1
                else:
                    if max_count < graph[z][x][y]:
                        max_count = graph[z][x][y]
    return max_count - 1


print(check())
