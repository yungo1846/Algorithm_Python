from collections import deque
import sys

N, M, K, X = list(map(int, sys.stdin.readline().rstrip().split()))

road = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    road[a].append(b)

distance = [-1] * (N+1)
distance[X] = 0

queue = deque([X])
while queue:
    q = queue.popleft()
    for i in road[q]:
        if distance[i] == -1:
            distance[i] = distance[q] + 1
            queue.append(i)

check = False
for i in range(1, N + 1):
    if distance[i] == K:
        print(i)
        check = True

if check == False:
    print(-1)
