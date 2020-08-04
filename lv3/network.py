def solution(n, computers):
    check_arr = [False] * n
    stack = [0]

    cnt = 1
    while False in check_arr:
        idx = stack.pop()
        check_arr[idx] = True

        for j in range(n):
            if not check_arr[j] and idx != j and computers[idx][j] == 1:
                stack.append(j)

        if len(stack) == 0 and False in check_arr:
            cnt = cnt+1

            for i in range(n):
                if not check_arr[i]:
                    stack.append(i)

    return cnt


n_input = 3
computers_input = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
solution(n_input, computers_input)
