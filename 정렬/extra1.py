test_case = int(input())
case_list = [[] for _ in range(test_case)]
for case in range(test_case):
    N = int(input())
    for _ in range(N):
        case_list[case].append(input())
    print(f"#{case+1}")
    case_list[case] = list(set(case_list[case]))
    case_list[case].sort(key=lambda x: (len(x), x))
    for i in case_list[case]:
        print(i)
