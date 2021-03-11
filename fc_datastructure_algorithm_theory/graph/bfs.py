import queue


def init_visied_dict(graph):
    visited = dict()
    for node in graph:
        visited[node] = False
    return visited


def bfs_search(graph, start_node):
    # 시간복잡도: O(V + E) -> 노드 수:V, 간선 수:E
    # linkedList로 구현된 경우에는 O(V+E), Array로 구현했을 경우 O(V^2)
    # 가중치 없는 그래프(간선의 가중치가 모두 1인 그래프)에서 최단 경로를 찾아준다.
    visited = init_visied_dict(graph)
    q = queue.Queue()
    # initialize first start node
    q.put(start_node)
    # start
    visited_node_order = list()
    count = 0
    while not q.empty():
        count += 1
        next_node = q.get()
        if not visited[next_node]:
            visited_node_order.append(next_node)
            visited[next_node] = True
            for linked_node in graph[next_node]:
                q.put(linked_node)
    print(f"visited order -> {visited_node_order}")
    print(count)


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
bfs_search(data, "A")
