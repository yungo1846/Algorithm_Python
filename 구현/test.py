from collections import deque

# 상하좌우 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, n, board, target):
    visited = [[0 for i in range(n)] for i in range(n)]
    visited[x][y] = 1
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            new_x = x+dx[i]
            new_y = y+dy[i]
            if new_x < 0:
                new_x = n-1
            elif new_x > n-1:
                new_x = 0
            if new_y < 0:
                new_y = n-1
            elif new_y > n-1:
                new_y = 0
            if visited[new_x][new_y] == 0:
                if board[new_x][new_y] == target:
                    return visited[x][y]+1, new_x, new_y
                q.append((new_x, new_y))
                visited[new_x][new_y] += visited[x][y] + 1


def solution(n, board):
    count = 0
    x, y = 0, 0
    target = 1
    while target <= n*n:
        num, x, y = bfs(x, y, n, board, target)
        print(num, x, y)
        target += 1
        count += num
    return count


print(solution(3, [[3, 5, 6], [9, 2, 7], [4, 1, 8]]))
