def solution(logs):
    log_length = 5000
    q_num_length = 100
    id_table = [[[] for i in range(0, q_num_length+1)]
                for i in range(0, log_length+1)]
    candidate = []
    cheater = []
    for log in logs:
        id, q_num, score = map(int, log.split())
        id_table[id][q_num] = score
    for table in id_table:
        if table != [[[] for i in range(0, q_num_length+1)] for i in range(0, log_length+1)]:
            candidate.append(table)
    for i in range(len(candidate)):
        for j in range(len(candidate)):
            if i != j and candidate[i] == candidate[j]:
                if i not in cheater:
                    cheater.append(i)
                    cheater.append(j)

    return cheater


logs = ["0001 3 95", "0001 5 90", "0001 5 100", "0002 3 95", "0001 7 80", "0001 8 80",
        "0001 10 90", "0002 10 90", "0002 7 80", "0002 8 80", "0002 5 100", "0003 99 90"]

print(solution(logs))
