import heapq


def dijkstra(graph: dict, start: str) -> (dict, dict):
    route = {node: [start] for node in graph}
    distance_dict = {node: float("inf") if node != start else 0 for node in graph}
    queue = []
    heapq.heappush(queue, [start, distance_dict[start]])
    while queue:
        current_node, current_distance = heapq.heappop(queue)
        if current_distance > distance_dict[current_node]:
            continue
        for adjacent_node, weight in graph[current_node].items():
            distance = weight + current_distance
            if distance < distance_dict[adjacent_node]:
                if current_node not in route[adjacent_node]:
                    route[adjacent_node].append(current_node)
                distance_dict[adjacent_node] = distance
                heapq.heappush(queue, [adjacent_node, distance])
    return distance_dict, route


mygraph = {
    "A": {"B": 8, "C": 1, "D": 2},
    "B": {},
    "C": {"B": 5, "D": 2},
    "D": {"E": 3, "F": 5},
    "E": {"F": 1},
    "F": {"A": 5},
}
distance, route = dijkstra(mygraph, "A")

print(distance)
print({key: "->".join(r) for key, r in route.items()})