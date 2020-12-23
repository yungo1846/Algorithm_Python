import bisect
import sys

N, X = list(map(int, input().split()))
nums = list(map(int, sys.stdin.readline().rstrip().split()))

if X in nums:
    index_start = bisect.bisect_right(nums, X - 1)
    index_end = bisect.bisect_right(nums, X)
    print(index_end - index_start)
else:
    print(-1)
