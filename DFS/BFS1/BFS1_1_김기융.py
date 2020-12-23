import sys
from collections import deque
n, m = list(map(int, input().split()))

graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

# 상하좌우 이동
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 벽을 뚤었는지 안 뚫었는지 판단하기 위해 삼차원 배열 사용
visited = [[[False for _ in range(m)] for _ in range(n)] for _ in range(2)]
distance = [[[1 for _ in range(m)] for _ in range(n)]
            for _ in range(2)]  # 문제에서 시작점도 거리를 1로 설정했으므로 1로 초기화


def bfs():
    visited[0][0][0] = True
    visited[1][0][0] = True
    q = deque()
    q.append((False, 0, 0))  # 벽을 뚫은 적이 있는지 여부, x 좌표, y 좌표
    while q:
        check, x, y = q.popleft()
        if not check:  # 이전에 벽을 뚫은 적이 없다면
            for i in range(4):
                new_x = x + dx[i]
                new_y = y + dy[i]
                if 0 <= new_x < n and 0 <= new_y < m:
                    # 벽 안 뚫고 다음으로
                    if graph[new_x][new_y] != 1 and not visited[0][new_x][new_y]:
                        q.append((False, new_x, new_y))
                        visited[0][new_x][new_y] = True
                        distance[0][new_x][new_y] = distance[0][x][y] + 1
                    if graph[new_x][new_y] == 1 and not visited[0][new_x][new_y]:
                        q.append((True, new_x, new_y))
                        visited[1][new_x][new_y] = True
                        distance[1][new_x][new_y] = distance[0][x][y] + 1
        # 벽을 이전에 한번 뚫었다면
        if check:
            for i in range(4):
                new_x = x + dx[i]
                new_y = y + dy[i]
                if 0 <= new_x < n and 0 <= new_y < m:
                    # 벽 안 뚫고 다음으로
                    if graph[new_x][new_y] != 1 and not visited[1][new_x][new_y]:
                        q.append((True, new_x, new_y))
                        visited[1][new_x][new_y] = True
                        distance[1][new_x][new_y] = distance[1][x][y] + 1

    # 탐색으로 얻은 벽을 뚫은 경우와 안 뚫은 경우 중 최소값을 선택
    # 이 때 결과값이 1이라면 도착지점까지 탐색이 이뤄지지 않은 것이므로 다른 경우를 린턴
    if distance[0][n - 1][m - 1] == 1:
        return distance[1][n - 1][m - 1]
    elif distance[1][n - 1][m - 1] == 1:
        return distance[0][n - 1][m - 1]
    else:
        return min(distance[0][n - 1][m - 1], distance[1][n - 1][m - 1])


# n과 m이 1로 주어진 경우는 특이케이스로 따로 처리
if n == 1 and m == 1:
    print(1)
else:
    min_dist = bfs()
    if min_dist == 1:
        print(-1)
    else:
        print(min_dist)
