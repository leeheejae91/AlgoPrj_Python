import re
import itertools


def solution(expression):
    num_arr = re.split('[*+-]', expression)
    ex_arr = []
    for i in expression:
        if i in ['+', '-', '*']:
            ex_arr.append(i)

    data_arr = []
    for i in range(len(ex_arr)):
        if len(data_arr) == 0:
            data_arr.append(num_arr[i])
        data_arr.append(ex_arr[i])
        data_arr.append(num_arr[i + 1])

    # 연산자 순위 조합
    exp_arr = list(itertools.permutations(['+', '-', '*'],3))

    answer = 0
    for exp in exp_arr:
        post_ex_arr = []
        ex_stack = []
        for data in data_arr:
            if data.isnumeric():
                post_ex_arr.append(data)
            else:
                if len(ex_stack) != 0:
                    if exp.index(data) > exp.index(ex_stack[len(ex_stack)-1]):
                        ex_stack.append(data)
                    else:
                        while len(ex_stack) != 0 and exp.index(ex_stack[len(ex_stack)-1]) >= exp.index(data) :
                            post_ex_arr.append(ex_stack.pop())
                        ex_stack.append(data)
                else:
                    ex_stack.append(data)

        while len(ex_stack) != 0:
            post_ex_arr.append(ex_stack.pop())

        # 계산
        cal_stack = []
        for i in post_ex_arr:
            if i.isnumeric():
                cal_stack.append(i)
            else:
                num2 = int(cal_stack.pop())
                num1 = int(cal_stack.pop())
                if i == '+':
                    cal_stack.append(num1 + num2)
                elif i == '-':
                    cal_stack.append(num1 - num2)
                elif i == '*':
                    cal_stack.append(num1 * num2)

        answer = max(abs(cal_stack[0]), answer)

    return answer


print(solution('100-200*300-500+20'))
