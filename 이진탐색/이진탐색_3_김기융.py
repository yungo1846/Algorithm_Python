
N = int(input())
nums = list(map(int, input().split()))
nums.sort()

start = 0
end = N-1
ans = nums[start] + nums[end]

s = 0
e = N - 1

while start < end:
    result = nums[start]+nums[end]  # 새로운 합
    if abs(result) < abs(ans):  # 0에 가까워야하므로 절댓값 계산
        ans = result
        s = start
        e = end
        if result == 0:  # 0이 제일 최소이므로 break
            break
    if result < 0:  # 결과가 음수면 시작지점을 오른쪽으로 이동하여 더 큰 값으로 계산
        start += 1
    else:
        end -= 1  # 결과가 양수면 끝지점을 왼쪽으로 이동하여 더 작은 값으로 계산
print(nums[s], nums[e])
