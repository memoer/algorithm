from functools import reduce

graph = dict()

graph["A"] = ["B", "C"]
graph["B"] = ["A", "D"]
graph["C"] = ["A", "G", "H", "I"]
graph["D"] = ["B", "E", "F"]
graph["E"] = ["D"]
graph["F"] = ["D"]
graph["G"] = ["C"]
graph["H"] = ["C"]
graph["I"] = ["C", "J"]
graph["J"] = ["I"]


def dfs(graph: dict, start_node: str) -> None:
    stack = [start_node]
    not_accessed_node_list = list(graph.keys())
    order = []
    while len(not_accessed_node_list) != 0:
        node = stack.pop()
        if not node in not_accessed_node_list:
            continue
        not_accessed_node_list.remove(node)
        stack += graph[node]
        order.append(node)
    print("->".join(order))


def dfs_2(graph: dict, start_node: str) -> None:
    visited, need_visit = list(), list()
    need_visit.append(start_node)
    order = list()
    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            order.append(node)
            visited.append(node)
            need_visit.extend(graph[node])
    print("->".join(order))


dfs_2(graph, "A")
