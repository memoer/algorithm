from heapq import *

data = {
    "A": {"B": 8, "C": 1, "D": 2},
    "B": {},
    "C": {"B": 5, "D": 2},
    "D": {"E": 3, "F": 5},
    "E": {"F": 1},
    "F": {"A": 5},
}


def dijkstra(data: dict, start_node: str) -> (list, list):
    distances = {
        node: float("inf") if node != start_node else 0
        for node in set(
            [node for node in data.keys()]
            + [node for value in data.values() for node in value.keys()]
        )
    }
    if not start_node in distances.keys():
        raise Exception(f"not {start_node} in {distances.keys()}")
    track = {node: [] for node in distances.keys()}
    queue = [(start_node, 0)]
    heapify(queue)
    while queue:
        cur_node, cur_distance = heappop(queue)
        for adjacent_node, adjacent_distance in data[cur_node].items():
            sum_distance = cur_distance + adjacent_distance
            if distances[adjacent_node] > sum_distance:
                distances[adjacent_node] = sum_distance
                heappush(queue, (adjacent_node, sum_distance))
                track[adjacent_node] = track[cur_node] + [cur_node]
    return distances, track


result, track = dijkstra(data, "A")
print(result)
print(track)
