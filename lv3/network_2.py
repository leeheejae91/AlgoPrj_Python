def solution(n, computers):
    answer = 0
    check_arr = [False] * n

    for i in computers:
        if not check_arr[i]:
            answer = answer + 1
            dfs(i, check_arr, computers)

    return answer


def dfs(i, check_arr, computers):
    check_arr[i] = True

    for j in range(len(computers[i])):
        if not check_arr[j] and i != j and computers[i][j] == 1:
            dfs(j, check_arr, computers)


n_input = 3
computers_input = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
solution(n_input, computers_input)
