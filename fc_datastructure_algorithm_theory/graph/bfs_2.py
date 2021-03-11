graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "G", "H", "I"],
    "D": ["B", "E", "F"],
    "E": ["D"],
    "F": ["D"],
    "G": ["C"],
    "H": ["C"],
    "I": ["C", "J"],
    "J": ["I"],
}


def bfs(data: dict, start_node: str) -> None:
    visited_node_list = []
    next_node_to_visit = [start_node]
    visit_order_node = []
    count = 0
    while next_node_to_visit:
        visited_node = next_node_to_visit.pop(0)
        count += 1
        if visited_node in visited_node_list:
            continue
        visited_node_list.append(visited_node)
        next_node_to_visit.extend(data[visited_node])
        visit_order_node.append(visited_node)
    print(",".join(visit_order_node), count)


# 노드 수(V) = 10
# 간선의 수(E) = 노드의 수 - 1 -> 10-1 = 9
# 시간복잡도 V+E
bfs(graph, "A")

