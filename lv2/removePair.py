def solution(s):
    answer = 0
    i = 0
    s_list = list(s)
    s_len  = len(s_list)
    while i < s_len - 1:
        if s_list[i] == s_list[i+1]:
            s_list.pop(i+1)
            s_list.pop(i)

            if i != 0: i -= 1
            s_len = len(s_list)
            continue

        i += 1

    print(s_list)
    if len(s_list) == 0:
        answer = 1

    return answer


input_str = 'baabaa'
solution(input_str)