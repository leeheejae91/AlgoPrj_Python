class DisjoinSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])

        return self.parent[v]

    def union(self, root1, root2):
        if self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        else:
            self.parent[root1] = root2

            if self.rank[root1] == self.rank[root2]:
                self.rank[root2] += 1


def kruskal(n, info):
    minimum = 0
    disjoint = DisjoinSet(n)
    result = []

    for data in sorted(info, key=lambda cost: cost[2]):
        v, u, weight = data
        root1 = disjoint.find(v)
        root2 = disjoint.find(u)

        if root1 != root2:
            disjoint.union(root1, root2)
            result.append(data)
            minimum += weight

    return result, minimum


print(kruskal(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))
