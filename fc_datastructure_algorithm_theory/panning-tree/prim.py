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


def init(data):
    edges = defaultdict(list)
    for weight, n1, n2 in data:
        edges[n1].append((weight, n1, n2))
        edges[n2].append((weight, n2, n1))
    return edges


def prim(start_node, data):
    mst = list()
    edges = init(data)
    # 현재 연결된 노드들 -> 처음에는 start_node 만
    connected_nodes = set(start_node)
    # Ex) A 노드에서의 간선 모음 -> (7, 'A', 'B'), (5, 'A', 'B')
    candidate_edges = edges[start_node]
    heapify(candidate_edges)
    while candidate_edges:
        weight, n1, n2 = heappop(candidate_edges)
        if n2 not in connected_nodes:
            connected_nodes.add(n2)
            mst.append((weight, n1, n2))
            for edge in edges[n2]:
                heappush(candidate_edges, edge)
    return mst


mst = prim("A", data)
print(mst)