<<<<<<< HEAD
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
=======
def solution(n, costs):
    costs.sort(key=lambda x: x[2])
    parent = list(range(n))
    answer = 0

    for data in costs:
        u, v, weight = data
        root1 = find_parent(u, parent)
        root2 = find_parent(v, parent)

        if root1 != root2:
            # 동일한 값을 갖는 모든 그룹을 다 업데이트 함
            root_min = min(root1, root2)
            for j in range(len(parent)):
                if parent[j] in [root1,root2]:
                    parent[j] = root_min
            answer += weight

    return answer


def find_parent(x, parent):
    if parent[x] != x:
        parent[x] = find_parent(parent[x], parent)

    return parent[x]


print(solution(5, [[0, 1, 1], [3, 4, 1], [1, 2, 2], [2, 3, 4]]))
>>>>>>> origin/master
