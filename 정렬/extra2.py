# 백준 10815번: 숫자 카드
import sys

N = int(input())
card1 = list(map(int, sys.stdin.readline().strip().split()))
M = int(input())
card2 = list(map(int, sys.stdin.readline().strip().split()))

card1.sort()


def binarySearch(target):
    start = 0
    end = len(card1) - 1
    while start <= end:
        mid = (start + end) // 2
        if card1[mid] == target:
            return True
        elif card1[mid] < target:
            start = mid + 1
        elif card1[mid] > target:
            end = mid - 1
    return False


for i in card2:
    if binarySearch(i):
        print("1", end=" ")
    else:
        print("0", end=" ")
