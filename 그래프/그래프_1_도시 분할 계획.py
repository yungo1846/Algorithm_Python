def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


v, e = map(int, input().split())
parent = [0] * (v + 1)
edges = []
result = 0

for i in range(1, v + 1):
    parent[i] = i

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()
last = 0

for edge in edges:
    cost, a, b = edge
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a != b:
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
        result += cost
        last = cost

print(result - last)
