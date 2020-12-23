N = int(input())
K = int(input())

start = 1
end = K

while start <= end:
    mid = (start + end) // 2

    result = 0
    for i in range(1, N + 1):
        result += min(mid // i, N)

    if result >= K:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)
