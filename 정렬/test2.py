import sys

test_case = int(input())
array = []
for case in range(test_case):
    input_data = sys.stdin.readline().strip().split()
    array.append([input_data[0], input_data[1]])

result = sorted(array, key=lambda x: x[1])

for name, score in result:
    print(name, end=" ")
