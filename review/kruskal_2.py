edges = [
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


class Kruskal:
    def __init__(self, edges: list):
        node_list = list(set([edge[1] for edge in edges] + [edge[2] for edge in edges]))
        self.edges = sorted(edges, key=lambda x: x[0])
        self.parent = {node: node for node in node_list}
        self.rank = {node: 0 for node in node_list}

    def get_root_node(self, node: str):
        if self.parent[node] != node:
            self.parent[node] = self.get_root_node(self.parent[node])
        return self.parent[node]

    def union(self, root_u: str, root_v: str):
        if root_u == root_v:
            return
        if self.rank[root_u] < self.rank[root_v]:
            self.parent[root_u] = root_v
        else:
            self.parent[root_v] = root_u
            if self.rank[root_u] == self.rank[root_v]:
                self.rank[root_u] += 1

    def run(self) -> list:
        result = list()
        for edge in self.edges:
            weight, node_u, node_v = edge
            root_node_u = self.get_root_node(node_u)
            root_node_v = self.get_root_node(node_v)
            self.union(root_node_u, root_node_v)
            if root_node_u != root_node_v:
                result.append(edge)
        return result


kruskal = Kruskal(edges)
result = kruskal.run()
print(result)