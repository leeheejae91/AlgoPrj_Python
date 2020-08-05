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
