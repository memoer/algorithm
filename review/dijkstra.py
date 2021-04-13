import heapq

graph = {
    "A": {"B": 8, "C": 1, "D": 2},
    "B": {},
    "C": {"B": 5, "D": 2},
    "D": {"E": 3, "F": 5},
    "E": {"F": 1},
    "F": {"A": 5},
}


def dijkstra(graph: dict, start_node) -> dict:
    distances = {node: float("inf") if start_node != node else 0 for node in graph.keys()}
    queue = []
    heapq.heappush(queue, [start_node, distances[start_node]])
    while queue:
        idx += 1
        node, distance = queue.pop(0)
        for (n, d) in graph[node].items():
            sum_d = distance + d
            if sum_d < distances[n]:
                distances[n] = sum_d
                heapq.heappush(queue, [n, sum_d])
    return distances


print(dijkstra(graph, "A"))
