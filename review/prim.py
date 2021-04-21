# 𝑂(𝐸𝑙𝑜𝑔𝑉) [E:간선수, V:노드수]
# 대표적인 신장트리 알고리즘 -> 크루스칼, 프림
# 탐욕 알고리즘 사용
# - 신장트리 -> 사이클 없음 / 가중치존재

# 1. 특정 지점부터 시작
# 2. 해당 정점에 연결된 가중치가 가장 작은 간선 선택
from collections import defaultdict
from heapq import *


class Prim:
    def __init__(self, data):
        self.data = data
        self.edge_list = list(set([edge[1] for edge in data] + [edge[2] for edge in data]))

    def run(self, start_node: str) -> list:
        result = list()
        # dict의 key 값 -> value를 list로 초기화
        adjacent_edges = defaultdict(list)
        # A 의 인접한 정점리스트를 모두 넣는다.
        # adjacent_edges["A"] = [(7,"A","B"), (5,"A","D")]
        for weight, n1, n2 in self.data:
            adjacent_edges[n1].append((weight, n1, n2))
            adjacent_edges[n2].append((weight, n2, n1))
        # 연결된 노드의 집합
        connected_nodes = set(start_node)
        # 다음으로 연결시킬 후보 정점들
        candidate_edge_list = adjacent_edges[start_node]
        # 가중치가 제일 작은 간선의 정점을 먼저 뽑아내야 하므로 heapq를 사용한다.
        heapify(candidate_edge_list)
        # 후보 정점이 없을 때까지
        while candidate_edge_list:
            # 가장 작은 가중치를 가진 정점을 가져온다.
            weight, n1, n2 = heappop(candidate_edge_list)
            # n2 [node] 가 연결되지 않았다면
            if n2 not in connected_nodes:
                # 추가
                connected_nodes.add(n2)
                result.append((weight, n1, n2))
                # D의 인접한 정점을 가져온다. -> [(7,"D","E"), (6,"D","F"), (5,"D","A"), (9,"D","B")]
                for edge in adjacent_edges[n2]:
                    # D를 기준으로 인접한 정점들을 모두 가져온다.
                    if edge[2] not in connected_nodes:
                        # edge[1]은 "D"로 고정, edge[2]->D와 연결된 노드들
                        # D와 연결된 노드들중 아직 연결되지 않은 노드만 후보정점에 넣는다.
                        heappush(candidate_edge_list, edge)
        return result


data = [
    (7, "A", "B"),
    (5, "A", "D"),
    (8, "B", "C"),
    (9, "B", "D"),
    (7, "B", "E"),
    (5, "C", "E"),
    (7, "D", "E"),
    (6, "D", "F"),
    (8, "E", "F"),
    (9, "E", "G"),
    (11, "F", "G"),
]
prim = Prim(data)
print(prim.run("A"))