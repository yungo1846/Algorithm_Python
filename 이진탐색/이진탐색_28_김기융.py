import sys

n = int(input())
nums = list(map(int, sys.stdin.readline().rstrip().split()))


def binary_search(start, end):  # 이진 탐색
    if start > end:
        return None

    mid = (start + end) // 2

    if nums[mid] == mid:  # 오름차순으로 정렬돼있으므로 중간값을 기준으로 이진탐색
        return mid
    if nums[mid] > mid:
        return binary_search(start, mid - 1)
    if nums[mid] < mid:
        return binary_search(mid + 1, end)


result = binary_search(0, n-1)
if result == None:
    print(-1)
else:
    print(result)
