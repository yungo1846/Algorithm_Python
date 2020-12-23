# pypy3로 통과
import sys
from collections import deque

n, m = list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = list(map(int, sys.stdin.readline().rstrip().split()))
    graph[a].append(b)  # 양방향 그래프이므로 1->3, 3->1을 추가해준다.
    graph[b].append(a)


def bfs(start):
    q = deque()
    q.append(start)
    result = []
    visited = [False] * (n + 1)
    visited[start] = True
    while q:
        v = q.popleft()
        result.append(v)
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
    return result


result = []
count = 0
for i in range(1, n+1):
    if i in result:  # 만약 result에 i가 존재한다면 생략하고 i+1 검색
        continue
    else:  # bfs를 통해 지나온 결과에 i가 존재하지 않으므로 연결요소 추가
        count += 1
        result += bfs(i)

print(count)
