def solution(s):
    return str(min([int(i) for i in s.split(" ")])) + ' ' + str(max([int(i) for i in s.split(" ") ]))


input_str = '-1 -2 -3 -4'
print(solution(input_str))
