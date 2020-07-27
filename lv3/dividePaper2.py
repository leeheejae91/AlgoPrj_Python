def solution(n):
    answer = []
    for i in range(n):
        if i == 0:
            answer.append(0)
        else:
            answer.append(0)
            for j in reversed(answer[:len(answer)-1]):
                if j == 0:
                    answer.append(1)
                else:
                    answer.append(0)

    return answer


num = 4
print(solution(num))