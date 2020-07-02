import itertools
import re


def solution(expression):
    ex_arr = []
    ex = []
    answer = 0
    x = 0

    for i in range(len(expression)):
        if not expression[i].isdigit():
            ex_arr.append(expression[x:i])
            ex_arr.append(expression[i])
            if expression[i] not in ex:
                ex.append(expression[i])
            x = i + 1

    # 마지막수 insert
    ex_arr.append(expression[x:len(expression)])

    ex_map = list(map(''.join, itertools.permutations(ex)))
    for i in ex_map:
        ex_prior = list(i)
        post_reg = []
        ex_stack = []

        # 후위연산식으로 변환
        for j in ex_arr:
            if j in ex:
                while len(ex_stack) != 0 and ex_prior.index(ex_stack[len(ex_stack) - 1]) <= ex_prior.index(j):
                    post_reg.append(ex_stack.pop())

                ex_stack.append(j)
            else:
                post_reg.append(int(j))

        while len(ex_stack) != 0:
            post_reg.append(ex_stack.pop())

        # 후위식 계산
        post_stack = []
        for k in post_reg:
            if k in ex and len(post_stack) != 0:
                b = post_stack.pop()
                a = post_stack.pop()
                if k == '-':
                    post_stack.append(a - b)
                elif k == '+':
                    post_stack.append(a + b)
                elif k == '*':
                    post_stack.append(a * b)
            else:
                post_stack.append(k)

        temp_answer = abs(post_stack.pop())
        if temp_answer > answer:
            answer = temp_answer

    return answer


input_t = '100-200*300-500+20'

solution(input_t)
