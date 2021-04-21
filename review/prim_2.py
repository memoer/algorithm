from heapq import *
from collections import defaultdict

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


def init_adjacent_edges(edge_list: list) -> dict:
    adjacent_edges = defaultdict(list)
    for edge in edge_list:
        weight, n1, n2 = edge
        adjacent_edges[n1].append((weight, n1, n2))
        adjacent_edges[n2].append((weight, n2, n1))
    return adjacent_edges


def prim(edge_list: list, start_node: str) -> list:
    connected_node_list = [start_node]
    adjacent_edges = init_adjacent_edges(edge_list)
    candidate_edge_list = [edge for edge in adjacent_edges[start_node]]
    result = []
    heapify(candidate_edge_list)
    while candidate_edge_list:
        weight, n1, n2 = heappop(candidate_edge_list)
        if not n2 in connected_node_list:
            connected_node_list.append(n2)
            result.append((weight, n1, n2))
            for edge in adjacent_edges[n2]:
                if not edge[2] in connected_node_list:
                    heappush(candidate_edge_list, edge)
    return result


result = prim(data, "A")
print(result)