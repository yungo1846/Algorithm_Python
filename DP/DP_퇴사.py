n = int(input())
t = []  # 소요되는 기간
p = []  # 금액
dp = []
for i in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)
    dp.append(b)
dp.append(0)  # 마지막 dp table 추가
for i in range(n - 1, -1, -1):  # 뒤에서부터 탐색
    if t[i] + i > n:  # 상담기간이 퇴사 날짜보다 긴 경우
        dp[i] = dp[i + 1]
    else:  # 현재 상담을 선택할지 않을지 결정
        dp[i] = max(dp[i + 1], p[i] + dp[i + t[i]])
print(dp[0])
