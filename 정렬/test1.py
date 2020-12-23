import sys

test_case = int(input())
array = []
for case in range(test_case):
    array.append(sys.stdin.readline().strip())

# 퀵 소트 리버스 버젼


def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left = [x for x in tail if x >= pivot]
    right = [x for x in tail if x < pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)


print(*quick_sort(array))
