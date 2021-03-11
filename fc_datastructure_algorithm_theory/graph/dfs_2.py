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


def bfs(data: dict, start_node) -> None:
    visited_node_list = []
    node_to_visit_list = [start_node]
    order_node_list = []
    count = 0
    while node_to_visit_list:
        count += 1
        visited_node = node_to_visit_list.pop()
        if visited_node in visited_node_list:
            continue
        node_to_visit_list.extend(data[visited_node])
        visited_node_list.append(visited_node)
        order_node_list.append(visited_node)
    print(order_node_list, count)


# 노드 수(V) = 10
# 간선의 수(E) = 노드의 수 - 1 -> 10-1 = 9
# 시간복잡도 V+E
bfs(graph, "A")
