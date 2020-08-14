def solution(n, edge):
    rank = [50000] * (n + 1)
    rank[1] = 1
    edge.sort(key=lambda x: x[1])
    edge.sort(key=lambda x: x[0])

    for data in edge:
        u, v = data
        val = min(rank[u], rank[v])
        if rank[u] < rank[v]:
            rank[v] = val + 1
        elif rank[u] > rank[v]:
            rank[u] = val + 1

    rank.pop(0)
    for i in range(len(rank)):
        if rank[i] == 50000:
            rank[i] = 0

    print(rank)
    return rank.count(max(rank))


print(solution(6, [[4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [1, 6], [5, 6], [5, 1]]))
