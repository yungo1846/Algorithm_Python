# python3로 통과
from collections import deque

n = int(input())    # NxN 공간의 크기

size_of_shark = 2   # 최초의 아기 상어의 몸집

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

# 상하좌우로 이동
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]


def bfs(x, y):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    visited[x][y] = 1
    q = deque()
    q.append((x, y))
    result = []
    while q:
        x, y = q.popleft()
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            # 배열을 벗어나지 않는 경우
            if 0 <= new_x < n and 0 <= new_y < n:
                # 이전에 탐색하지 않았고 상어의 크기와 작거나 같은 경우 이동 가능
                if graph[new_x][new_y] <= size_of_shark and visited[new_x][new_y] == 0:
                    # 상어의 크기보다 작은 경우 먹기가 가능
                    if graph[new_x][new_y] < size_of_shark and graph[new_x][new_y] != 0:
                        # 먹었다는 사실과 위치를 결과에 추가
                        result.append((new_x, new_y, visited[x][y], True))
                    else:
                        q.append((new_x, new_y))
                        # 탐색할 때까지 소모된 시간을 저장
                        visited[new_x][new_y] = visited[x][y] + 1
    # 상어가 먹이를 하나도 먹지 못하는 경우
    if len(result) == 0:
        return - 1, -1, -1, -1
    else:
        # 상어가 물고기를 먹을 수 있는 가능한 경우 중 가까운 거리 순으로 정렬
        # 이 때 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 가장 왼쪽에 있는 물고기 순으로
        result = sorted(result, key=lambda x: (x[2], x[0], x[1]))
        return result[0]


eat = False  # 상어가 물고기를 먹었는지 체크
count = 0  # 상어가 먹은 물고기 수, 몸집이 커지면 0으로 초기화
total_sec = 0  # 모든 물고기를 먹을 때까지 걸리는 시간


def is_possible_to_eat():  # 상어가 물고기를 먹을 수 있는가 체크하는 함수
    global count, graph, size_of_shark, total_sec
    for x in range(n):
        for y in range(n):
            if graph[x][y] == 9:  # 상어의 위치를 발견하면 bfs 호출
                new_x, new_y, sec, eat = bfs(x, y)
                if new_x == -1:  # 상어가 물고기를 먹지 못함.
                    return False
                else:  # 물고기를 먹을 수 있다면
                    if eat:
                        count += 1
                        total_sec += sec
                    if count == size_of_shark:
                        size_of_shark += 1
                        count = 0
                    graph[x][y] = 0  # 현재 있던 상어의 위치 초기화
                    graph[new_x][new_y] = 9  # 상어가 이동할 곳에 상어위치를 표시
                    return True
    return False


while True:  # 상어가 상하좌우로 이동할 수 있기 때문에 조건에 만족할 때까지 계속 반복.
    if is_possible_to_eat():
        continue
    else:
        break

print(total_sec)
