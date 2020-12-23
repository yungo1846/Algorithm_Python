string = input()

zero_count = 0
one_count = 0
for index, letter in enumerate(string):
    if index == 0:  # 첫 글자
        pre_letter = letter
        continue
    if pre_letter != letter:
        if pre_letter == '0':
            zero_count += 1
        else:
            one_count += 1
    if index == len(string) - 1:  # 끝 글자
        if letter == '0':
            zero_count += 1
        else:
            one_count += 1
    pre_letter = letter

print(min(zero_count, one_count))
