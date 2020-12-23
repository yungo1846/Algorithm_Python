N, M = list(map(int, input().split()))

matrix1 = []
matrix2 = []
for i in range(N):
    line = input()
    matrix = []
    for each in line:
        matrix.append(each)
    matrix1.append(matrix)
for i in range(N):
    matrix = []
    for each in line:
        matrix.append(each)
    matrix2.append(matrix)

reverse_count = 0

while True:
    if N < 3 or M < 3:
        reverse_count = -1
        break

    if matrix1 == matrix2:
        break

    if reverse_count > 1000:
        reverse_count = -1
        break

    count_list = []
    for i in range(N-2):
        for j in range(M-2):
            count = 0
            for x in range(i, i + 3):
                for y in range(j, j + 3):
                    if matrix1[x][y] != matrix2[x][y]:
                        count += 1
                count_list.append([count, i, j])

    max_count = max(count_list)
    for i in range(max_count[1], max_count[1] + 3):
        for j in range(max_count[2], max_count[2] + 3):
            if matrix1[i][j] == "0":
                matrix1[i][j] = "1"
            else:
                matrix1[i][j] = "0"
    reverse_count += 1


print(reverse_count)
