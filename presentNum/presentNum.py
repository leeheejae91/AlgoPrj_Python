def solution(n):
    answer = 1
    for i in range(1,n):
        temp = i
        sum = 0

        while True:
            if sum == n:
                answer = answer +1
                break
            elif sum > n :
                break


            sum = sum + temp
            temp = temp + 1

    return answer


number = 15

print(solution(number))

