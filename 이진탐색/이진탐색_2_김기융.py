def solution(d, budget):
    d.sort()
    total = 0
    count = 0
    for i in d:
        if total + i <= budget:
            total += i
            count += 1
        else:
            break
    return count
