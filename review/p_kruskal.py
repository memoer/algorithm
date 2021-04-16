# O(E log E) [E:간선수]
# 대표적인 신장트리 알고리즘 -> 크루스칼, 프림
# 탐욕 알고리즘 사용
# - 신장트리 -> 사이클 없음 / 가중치존재

# 1. 가장 작은 가중치부터 시작
# 2. 그 다음 가장 작은 가중치 -> 반복

# - union / find 를 통해 알고리즘 구현
# - union-by-rank / path-compression 을 통해 알고리즘 개선
class Kruskal:
    def __init__(self, data: list):
        data.sort()
        self.data = data
        self.parent = {edge[1]: edge[1] for edge in data}
        self.rank = {edge[1]: 0 for edge in data}

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node_v, node_u):
        if self.rank[node_v] > self.rank[node_u]:
            self.parent[node_u] = node_v
        else:
            self.parent[node_v] = node_u
            if self.rank[node_v] == self.rank[node_u]:
                self.rank[node_u] += 1

    def run(self):
        result = list()
        for edge in self.data:
            weight, node_v, node_u = edge
            root_v, root_u = self.find(node_v), self.find(node_u)
            if root_v != root_u:
                self.union(root_v, root_u)
                result.append(edge)
        return result


sample = [
    (7, "A", "B"),
    (5, "A", "D"),
    (7, "B", "A"),
    (8, "B", "C"),
    (9, "B", "D"),
    (7, "B", "E"),
    (8, "C", "B"),
    (5, "C", "E"),
    (5, "D", "A"),
    (9, "D", "B"),
    (7, "D", "E"),
    (6, "D", "F"),
    (7, "E", "B"),
    (5, "E", "C"),
    (7, "E", "D"),
    (8, "E", "F"),
    (9, "E", "G"),
    (6, "F", "D"),
    (8, "F", "E"),
    (11, "F", "G"),
    (9, "G", "E"),
    (11, "G", "F"),
]
kruskal = Kruskal(sample)
print(kruskal.run())
