import time
import random

array = []
for i in range(10000):
    array.append(random.randint(1, 10000))


# 선택 정렬 - data 10,000개인 경우 2.15초 소요
def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i+1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        temp = array[i]
        array[i] = array[min_index]
        array[min_index] = temp
    return array


# 삽입 정렬 - data 10,000개인 경우 4.5초 소요
def insertion_sort(array):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j-1]:
                temp = array[j]
                array[j] = array[j - 1]
                array[j-1] = temp
            else:
                break
    return array


# 퀵 정렬 - data 10,000개인 경우 0.1초 소요
def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left = [i for i in tail if i < pivot]
    right = [j for j in tail if j >= pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)


# 계수 정렬 - data 10,000개인 경우 1.43초 소요
def counting_sort(array):
    count = [0] * (max(array) + 1)

    for i in array:
        count[i] += 1

    for i in range(len(count)):
        for j in range(count[i]):
            print(i, end=" ")


# 병합 정렬 - data 10,000개인 경우 0.27초 소요
def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    return result

# 선택 정렬
# start_t1 = time.time()
# print(selection_sort(array))
# end_t1 = time.time()
# print(end_t1-start_t1)

# 삽입 정렬
# start_t1 = time.time()
# print(insertion_sort(array))
# end_t1 = time.time()
# print(end_t1-start_t1)


# # 퀵 정렬
#start_t1 = time.time()
# print(quick_sort(array))
#end_t1 = time.time()
# print(end_t1-start_t1)

# 계수 정렬
# start_t1 = time.time()
# counting_sort(array)
# end_t1 = time.time()
# print(end_t1-start_t1)

# 병합 정렬
# start_t1 = time.time()
# print(merge_sort(array))
# end_t1 = time.time()
# print(end_t1-start_t1)
