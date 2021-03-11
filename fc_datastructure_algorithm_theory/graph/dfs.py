import queue


def init_visited(graph):
    visited = dict()
    for node in graph:
        visited[node] = False
    return visited


def dfs_search(graph, start_node):
    # 시간복잡도 : O(V + E) -> 노드 수:V, 간선 수:E
    if not start_node in graph:
        return False
    visited_order = list()
    visited = init_visited(graph)
    stack = queue.LifoQueue()
    stack.put(start_node)
    while not stack.empty():
        next_node = stack.get()
        if not visited[next_node]:
            visited_order.append(next_node)
            visited[next_node] = True
            for linked_node in graph[next_node]:
                stack.put(linked_node)
    print(visited_order)


data = dict()
data["A"] = ["B", "C"]
data["B"] = ["A", "D"]
data["C"] = ["A", "G", "H", "I"]
data["D"] = ["B", "E", "F"]
data["E"] = ["D"]
data["F"] = ["D"]
data["G"] = ["C"]
data["H"] = ["C"]
data["I"] = ["C", "J"]
data["J"] = ["I"]
dfs_search(data, "A")
