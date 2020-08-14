import copy


def solution(n, costs):
    cost_map = []
    answer_map = []

    for _ in range(n):
        cost_map.append([0] * n)

    answer_map = copy.deepcopy(cost_map)

    for i in costs:
        cost_map[i[0]][i[1]] = i[2]
        cost_map[i[1]][i[0]] = i[2]

    check_arr = [False] * n
    cur = 0
    queue = []

    check_arr[cur] = True
    for i in range(cost_map[cur]):
        if cost_map[cur][i] != 0 and not check_arr[i]:
            queue.append(i)


    answer = 0
    return answer

island = [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]
n_input = 4
solution(n_input, island)
