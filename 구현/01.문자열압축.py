def solution(s):
    result_list = []
    for i in range(1, (len(s) // 2 + 1)):
        count = 0
        string = ""
        split_list = []
        for j in range(len(s)):
            string += s[j]
            count += 1
            if count == i:
                split_list.append(string)
                string = ""
                count = 0
        dup_count = 1  # 중복의 개수
        result = ""
        print(split_list)
        for k in range(len(split_list)-1):
            if split_list[k] == split_list[k + 1]:
                dup_count += 1
            else:
                if dup_count != 1:
                    result += str(dup_count) + split_list[k]
                else:
                    result += split_list[k]
                dup_count = 1
        if result != "":
            result_list.append(result)
        else:
            result_list.append(s)
    return result_list


s1 = "abcabcabcabcdededededede"
print(solution(s1))
