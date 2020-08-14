import collections


def solution(n, edge):
    answer = 0
    visited = []
    queue = collections.deque([1])

    while queue:
        l = len(queue)

        for _ in range(l):
            x = queue.popleft()
            if x not in visited:
                for data in edge:
                    u, v = data
                    if u == x and v not in queue and v not in visited:
                        queue.append(v)
                    if v == x and u not in queue and u not in visited:
                        queue.append(u)
            visited.append(x)

    return len(l)


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
