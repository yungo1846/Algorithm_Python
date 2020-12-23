
N, K = list(map(int, input().split()))
array_A = list(map(int, input().split()))
array_B = list(map(int, input().split()))

array_A.sort()
array_B.sort()

for i in range(K):
    if array_A[i] > array_B[-1 - i]:
        array_A[i] = array_B[-1-i]

print(sum(array_A))
