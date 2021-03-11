"""
단일 출발 최단 경로 문제
- 특정 노드 u와 그래프 내 다른 모든 노드 각각의 가장 짧은 경로를 찾는 문제
  다익스트라 알고리즘
  - 첫 정점을 기준으로 연결되어 있는 정점들을 추가해 가며, 최단 거리를 생긴하는 기법
  - BFS와 유사
"""
import heapq

data = {
    "A": {"B": 8, "C": 1, "D": 2},
    "B": {},
    "C": {"B": 5, "D": 2},
    "D": {"E": 3, "F": 5},
    "E": {"F": 1},
    "F": {"A": 5},
}


def init_dijkstra(graph: dict, start_node: str) -> (dict, list, dict):
    route = {node: [start_node] for node in graph}
    distances = {node: float("inf") for node in graph}
    distances[start_node] = 0
    queue = []
    heapq.heappush(queue, [0, start_node])
    return distances, queue, route


def dijkstra(graph: dict, start_node: str) -> (dict, dict):
    """
    1. 각 노드마다 인접한 간선들을 모두 검사 -> O(E) , E: 간선
    2. 우선순위 큐에 가장 많은 노드, 거리 정보가 들어가는 경우, 우선 순위 큐에 노드/거리 정보를 넣고 삭제하는 과정이 최악의 시간이 걸림
      -> 우선순위 큐(힙)을 유지하는 작업은 -> O(ElogE)
    다익스트라 -> O(E) + O(ElogE) = O(ElogE)
    """
    if not start_node in graph:
        return {}, {}
    distances, queue, route = init_dijkstra(graph, start_node)
    count = 0
    while len(queue) != 0:
        node_distance, node_name = heapq.heappop(queue)
        if node_distance > distances[node_name]:
            continue
        for linked_node, weight in graph[node_name].items():
            count += 1
            pre_distance = distances[linked_node]
            new_distance = node_distance + weight
            # 기존에 있던 가중치보다 더 작을 경우에만 update
            if pre_distance > new_distance:
                # 가중치 테이블 업데이트
                distances[linked_node] = new_distance
                # 업데이트 후, 큐에 push
                heapq.heappush(queue, [new_distance, linked_node])
                if node_name != start_node:
                    route[linked_node].append(node_name)
    for key in route:
        route[key] = " -> ".join(route[key])
    print(count)
    return distances, route


dist, route = dijkstra(data, "A")
print(dist)
print(route)
