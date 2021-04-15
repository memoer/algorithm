class Kruskal:
    def __init__(self, data) -> None:
        data.sort(key=lambda x: x[0])
        self.data = data
        self.parent = {edge[1]: edge[1] for edge in data}
        self.rank = {edge[1]: 0 for edge in data}

    def find_root(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find_root(self.parent[node])
        return self.parent[node]

    def union(self, root_v, root_u):
        if self.rank[root_v] > self.rank[root_u]:
            self.parent[root_u] = root_v
        else:
            self.parent[root_v] = root_u
            if self.rank[root_v] == self.rank[root_u]:
                self.rank[root_u] += 1

    def run(self) -> list:
        result = list()
        for edge in self.data:
            weight, node_v, node_u = edge
            root_u = self.find_root(node_v)
            root_v = self.find_root(node_u)
            if root_u != root_v:
                self.union(root_u, root_v)
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