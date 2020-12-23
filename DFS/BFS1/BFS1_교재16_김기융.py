from itertools import combinations  # 조합을 위해 사용
from collections import deque
from copy import deepcopy  # 이차원 배열 복사를 위해 사용

n, m = list(map(int, input().split()))
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

safe = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            safe.append((i, j))

# 상하좌우 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(graph, x, y):
    visited = [[False for _ in range(m)] for _ in range(n)]
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        visited[x][y] = True
        for i in range(4):  # 상하좌우 검색
            new_x = x + dx[i]
            new_y = y + dy[i]
            if new_x < 0 or new_x >= n or new_y < 0 or new_y >= m:  # 배열의 크기를 벗어나는 경우 제외
                continue
            if graph[new_x][new_y] != 0:
                continue
            if not visited[new_x][new_y]:
                graph[new_x][new_y] = 2
                q.append((new_x, new_y))
    return graph


combs = list(combinations(safe, 3))  # 벽을 3개 세우는 경우 찾기
max_count = 0
for comb in combs:
    new_graph = deepcopy(graph)  # 이차원 배열 복사
    for x, y in comb:
        new_graph[x][y] = 1
    for x in range(n):
        for y in range(m):
            if new_graph[x][y] == 2:
                new_graph = bfs(new_graph, x, y)

    # 안전 지대 0 체크
    count = 0
    for x in range(n):
        for y in range(m):
            if new_graph[x][y] == 0:
                count += 1

    # 가장 안전지대의 수가 많은 것을 선택
    max_count = max(max_count, count)

print(max_count)
