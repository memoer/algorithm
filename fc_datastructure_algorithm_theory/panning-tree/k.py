data = [
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
    def __init__(self, data: list):
        self.edge_list = sorted(data, key=lambda x: x[0])
        self.node_list = list(set([edge[1] for edge in data]))
        self.parent = {node: node for node in self.node_list}
        self.rank = {node: 0 for node in self.node_list}

    def find(self, node: str) -> str:
        if node != self.parent[node]:
            root_node = self.find(self.parent[node])
            if root_node != self.parent[node]:
                self.parent[node] = root_node
        return self.parent[node]

    def union(self, node_x: str, node_y: str) -> None:
        root_x = self.find(node_x)
        root_y = self.find(node_y)
        self.parent[root_x] = root_y

    def get_mst(self):
        mst = []
        for edge in self.edge_list:
            weight, node_x, node_y = edge
            if self.find(node_x) != self.find(node_y):
                self.union(node_x, node_y)
                mst.append(edge)
        return mst


kruskal = Kruskal(data)
mst = kruskal.get_mst()
print(mst)