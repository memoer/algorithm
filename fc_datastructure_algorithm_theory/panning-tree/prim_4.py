# 직접 구현한 것.
from collections import defaultdict
from heapq import *

data = [
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


class Prim:
    def __init__(self, data: list) -> None:
        # 그래프
        self.edge_list = data
        # 그래프에 존재하는 노드들
        self.existed_node_list = self.get_existed_node_list(data)
        # 한 노드에 대해 연결된 정보
        # "A" 일 경우 ->"A": [(3, "A", "B")]의 형태로 저장된다.
        self.adjacent_edge_list = self.get_adjacent_edge_list(data)

    def get_existed_node_list(self, data: list) -> set:
        existed_node_list = set()
        for edge in data:
            existed_node_list.add(edge[1])
            existed_node_list.add(edge[2])
        return existed_node_list

    def get_adjacent_edge_list(self, data: list) -> list:
        adjacent_edge_list = defaultdict(list)
        for weight, n1, n2 in data:
            adjacent_edge_list[n1].append((weight, n1, n2))
            adjacent_edge_list[n2].append((weight, n2, n1))
        return adjacent_edge_list

    def init_mst(self, start_node):
        # 최소 신장 트리 정보
        mst = []
        # 연결된 노드들
        connected_node_list = [start_node]
        # 어떠한 노드에 대한 인접한 노드들에 대해서 연결할 수 있는 엣지들
        candidate_node_list = self.adjacent_edge_list[start_node]
        heapify(candidate_node_list)
        return mst, connected_node_list, candidate_node_list

    def get_mst(self, start_node) -> list:
        if start_node not in self.existed_node_list:
            raise Exception(f"start_node[{start_node}] is not in node_list")
        mst, connected_node_list, candidate_node_list = self.init_mst(start_node)
        all_connected = lambda x, y: len(x) == len(y)
        while not all_connected(connected_node_list, self.existed_node_list):
            weight, node_x, node_y = heappop(candidate_node_list)
            if node_y not in connected_node_list:
                connected_node_list.append(node_y)
                mst.append((weight, node_x, node_y))
                for edge in self.adjacent_edge_list[node_y]:
                    if edge[2] not in connected_node_list:
                        heappush(candidate_node_list, edge)
        return mst


prim = Prim(data)
mst = prim.get_mst("A")
print(mst)
