from itertools import permutations
from collections import deque
import sys

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def crash(x, y, matrix):  # bfs
    visited = [[0 for _ in range(H)] for _ in range(W)]
    visited[x][y] = 1
    q = deque()
    q.append((x, y))
    num = matrix[x][y]
    while q:
        x, y = q.popleft()
        matrix[x][y] = 0
        for i in range(4):
            for j in range(num-1):
                new_x = x + dx[i]
                new_y = y + dy[i]
                # 배열을 벗어나지 않는 경우
                if 0 <= new_x < H and 0 <= new_y < W:
                    if not visited[new_x][new_y] and matrix[new_x][new_y] != 0:
                        visited[new_x][new_y] = 1
                        q.append((new_x, new_y))

    return matrix


def count_block(result):
    count = 0
    for x in range(H):
        for y in range(W):
            if result[x][y] != 0:
                count += 1
    return count


test = int(input())
for test_case in range(test):
    graph = []
    N, W, H = list(map(int, input().split()))
    for i in range(H):
        graph.append(list(map(int, sys.stdin.readline().strip().split())))

    items = [i for i in range(W)]
    perm_list = list(permutations(items, N))
    for perm in perm_list:  # perm=(0,1,2)
        result = graph
        for seq in range(N):  # seq = 0 -> 1 -> 2
            i = 0
            while i < H:
                if graph[i][perm[seq]] == 0:
                    i += 1
                else:
                    break
            if i == H:  # 해당 열에 아무 블록도 없는 경우
                i = -1
            if i != -1:
                print(perm, seq, i)
                result = crash(perm[seq], i, result)
                num_of_left_block = count_block(result)
                print(num_of_left_block)
