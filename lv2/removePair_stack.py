def solution(s):
    answer = 0
    s_stack = []
    s_list = list(s)

    while len(s_list) != 0:
        s_stack.append(s_list.pop())


    return answer


input_str = 'baabaa'
solution(input_str)