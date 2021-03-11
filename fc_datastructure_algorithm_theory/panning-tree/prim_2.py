# 직접구현한 것
import heapq
from collections import defaultdict


class Prim:
    def __init__(self, data: list) -> None:
        self.edge_list = data
        self.node_list = list(set([edge[1] for edge in data] + [edge[2] for edge in data]))
        self.parent = {node: node for node in self.node_list}
        self.rank = {node: 0 for node in self.node_list}

    def find(self, node: str) -> str:
        parent_node = self.parent[node]
        if node != parent_node:
            root_node = self.find(parent_node)
            if parent_node != root_node:
                self.parent[node] = root_node
        return self.parent[node]

    def union(self, node_x: str, node_y: str) -> None:
        root_x = self.find(node_x)
        rank_x = self.rank[root_x]
        root_y = self.find(node_y)
        rank_y = self.rank[root_y]
        if rank_x > rank_y:
            self.parent[root_y] = root_x
        else:
            self.parent[root_x] = root_y
            if rank_x == rank_y:
                self.rank[root_y] += 1

    def get_mst(self, start_node: str) -> list:
        if start_node not in self.node_list:
            raise Exception(f"start_node[{start_node}] is not in node_list")
        mst = []
        connected_node_list = set()
        candidate_edge_list = [edge for edge in self.edge_list if edge[1] == start_node]
        heapq.heapify(candidate_edge_list)
        while len(connected_node_list) != len(self.node_list):
            popped_edge = heapq.heappop(candidate_edge_list)
            if self.find(popped_edge[1]) != self.find(popped_edge[2]):
                self.union(popped_edge[1], popped_edge[2])
                connected_node_list.add(popped_edge[1])
                connected_node_list.add(popped_edge[2])
                for edge in [
                    edge
                    for edge in self.edge_list
                    if edge != popped_edge
                    and (edge[1] == popped_edge[2] or edge[2] == popped_edge[2])
                ]:
                    heapq.heappush(candidate_edge_list, edge)
                mst.append(popped_edge)
        return mst


my_edges = [
    (7, "A", "B"),
    (5, "A", "D"),
    (8, "B", "C"),
    (9, "B", "D"),
    (7, "B", "E"),
    (5, "C", "E"),
    (7, "D", "E"),
    (6, "D", "F"),
    (8, "E", "F"),
    (9, "E", "G"),
    (11, "F", "G"),
]

prim = Prim(my_edges)
mst = prim.get_mst("A")
print(mst)