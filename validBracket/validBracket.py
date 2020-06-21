input_data = '(()('


def solution(s):
    input_arr = list(s)
    temp_stack = []

    for i in input_data:
        if i == '(':
            temp_stack.append(i)
        elif i == ')':
            if len(temp_stack) == 0:
                return False
            else :
                temp_stack.pop()

    if len(temp_stack) == 0 :
        return True

    else :
        return False


print solution(input_data)

