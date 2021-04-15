import heapq

graph = {
    "A": {"B": 8, "C": 1, "D": 2},
    "B": {},
    "C": {"B": 5, "D": 2},
    "D": {"E": 3, "F": 5},
    "E": {"F": 1},
    "F": {"A": 5},
}


def dijkstra(graph: dict, start_node: str) -> dict:
    queue = [[start_node, 0]]
    distances = {node: float("inf") if node != start_node else 0 for node in graph.keys()}
    heapq.heapify(queue)
    track = {node: [] for node in graph.keys()}
    while queue:
        current_node, current_distance = heapq.heappop(queue)
        for adjacent_node, adjacent_distance in graph[current_node].items():
            sum_distance = adjacent_distance + current_distance
            if sum_distance < distances[adjacent_node]:
                track[adjacent_node] = track[current_node] + [adjacent_node]
                distances[adjacent_node] = sum_distance
                heapq.heappush(queue, [adjacent_node, sum_distance])
    return distances, track


distances, track = dijkstra(graph, "A")
print(track)