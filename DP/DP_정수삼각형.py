
size = int(input())
triangle = []
for i in range(0, size):
    triangle.append(list(map(int, input().split())))

result = [[0 for i in range(size)] for i in range(size)]  # dp table 생성
result[0][0] = triangle[0][0]  # 삼각형의 최상단값 설정
for i in range(1, size):
    for j in range(0, len(triangle[i])):
        if j == 0:  # 맨 왼쪽의 경우
            result[j][i] = result[j][i - 1] + triangle[i][j]
        elif j == len(triangle[i]) - 1:  # 맨 오른쪽의 경우
            result[j][i] = result[j - 1][i - 1] + triangle[i][j]
        else:  # 그 외
            result[j][i] = max(result[j - 1][i - 1] +
                               triangle[i][j], result[j][i - 1]+triangle[i][j])

max_value = -9999
for num_list in result:
    max_value = max(max_value, num_list[-1])
print(max_value)
