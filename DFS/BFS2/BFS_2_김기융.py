# Puyo Puyo

from collections import deque

graph = []

for _ in range(12):
    graph.append(list(input()))

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, color):
    visited = [[0 for _ in range(6)] for _ in range(12)]
    visited[x][y] = 1
    q = deque()
    q.append((x, y))
    result = [[x, y]]  # .으로 바꿔줘야할 좌표 저장
    count = 1  # 인접한 같은 색깔의 블록 개수 파악
    while q:
        x, y = q.popleft()
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            # 배열을 벗어나지 않는 경우
            if 0 <= new_x < 12 and 0 <= new_y < 6:
                if not visited[new_x][new_y] and graph[new_x][new_y] == color:
                    visited[new_x][new_y] = 1
                    count += 1
                    q.append((new_x, new_y))
                    result.append((new_x, new_y))

    return count, result

# 블록이 터지고 나서 위에 블록을 아래로 내리기


def rePositioning():
    for x in range(11, -1, -1):
        for y in range(5, -1, -1):
            if graph[x][y] != '.':
                i = x
                while i < 11:  # .이 어디까지 있는지 파악
                    if graph[i+1][y] == '.':
                        i += 1
                    else:
                        break
                if graph[i][y] == '.':  # 이 조건을 안 넣으면 점이 아닌 문자여도
                    graph[i][y] = graph[x][y]  # 점으로 바꿔버리기 때문에 추가
                    graph[x][y] = '.'


chain_count = 0
is_bomb = False  # 4개 이상 붙어있는 것이 한개라도 있는 경우
while True:
    for x in range(12):
        for y in range(6):
            if graph[x][y] != '.':
                count, result = bfs(x, y, graph[x][y])
                if count >= 4:
                    is_bomb = True
                    for del_x, del_y in result:  # del_x, del_y는 '.'으로 바꿀 좌표
                        graph[del_x][del_y] = '.'
    if is_bomb:
        chain_count += 1
        rePositioning()
        is_bomb = False
    else:  # 아무것도 터지지 않았다는 의미는 더 이상 진행하지 않아도 된다는 뜻
        break


print(chain_count)
