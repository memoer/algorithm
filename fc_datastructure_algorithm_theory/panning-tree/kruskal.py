data = {
    # 노드
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    # 간선
    'edges': [
        # 가중치, X - Y
        (7, 'A', 'B'),
        (5, 'A', 'D'),
        (7, 'B', 'A'),
        (8, 'B', 'C'),
        (9, 'B', 'D'),
        (7, 'B', 'E'),
        (8, 'C', 'B'),
        (5, 'C', 'E'),
        (5, 'D', 'A'),
        (9, 'D', 'B'),
        (7, 'D', 'E'),
        (6, 'D', 'F'),
        (7, 'E', 'B'),
        (5, 'E', 'C'),
        (7, 'E', 'D'),
        (8, 'E', 'F'),
        (9, 'E', 'G'),
        (6, 'F', 'D'),
        (8, 'F', 'E'),
        (11, 'F', 'G'),
        (9, 'G', 'E'),
        (11, 'G', 'F')
    ]
}


def init(graph: dict) -> (dict, dict):
  parent = dict()
  rank = dict()
  for node in graph['vertices']:
    parent[node] = node
    rank[node] = 0
  return parent, rank


def find(parent: dict, node: str) -> str:
  # path compression
  # Ex)
  # - parent['A'] = 'A' 라면 노드 A의 root node는 없다
  #   오로지 자기만 있는 것.
  # - parent['A'] = 'B' 라면 노드 A의 root node는 'B'라는 것.
  #   여기서 다시, B의 부모 노드를 찾으러 간다 -> find(parent, parent[node])
  if node != parent[node]:
    parent[node] = find(parent, parent[node])
  return parent[node]


def union(rank: dict, parent: dict, node_v: str, node_u: str):
  # union by rank
  root_v = find(parent, node_v)
  root_u = find(parent, node_u)
  if rank[root_v] > rank[root_u]:
    parent[root_u] = root_v
  else:
    parent[root_v] = root_u
    if rank[root_v] == rank[root_u]:
      rank[root_u] += 1


def kruskal(graph: dict) -> dict:
  # initialize
  parent, rank = init(graph)
  # result data
  mst = list()
  # sort
  graph['edges'].sort(key=lambda item: item[0])
  # start
  for edge in graph['edges']:
    # 이미 가중치에 대해 sorting을 시켜 줬기 때문에 가중치에 대한 비교는 하지 않는다.
    _, node_v, node_u = edge
    if find(parent, node_v) != find(parent, node_u):
      union(rank, parent, node_v, node_u)
      mst.append(edge)
  return mst


print(kruskal(data))
