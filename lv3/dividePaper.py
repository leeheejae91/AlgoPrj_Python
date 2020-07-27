def solution(n):
    answer = []
    for i in range(1, n + 1):
        if i == 1:
            answer.append(0)
        elif i == 2:
            answer.insert(0,0)
            answer.append(1)
        else:
            temp_arr = []
            side = 2 ** (i-3)
            mid = 2 ** (i-2) - 1

            for j in range(side):
                temp_arr.append(0)
                temp_arr.append(answer.pop(0))
                temp_arr.append(1)

            for j in range(mid):
                temp_arr.append(answer.pop(0))

            for j in range(side):
                temp_arr.append(0)
                temp_arr.append(answer.pop(0))
                temp_arr.append(1)

            answer = temp_arr

    return answer


num = 4
print(solution(num))