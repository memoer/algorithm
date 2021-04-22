n = int(input())


def find(f: str) -> str:
    if parent[f] != f:
        parent[f] = find(parent[f])
    return parent[f]


def union(a: str, b: str) -> None:
    root_a = find(a)
    root_b = find(b)
    if root_a != root_b:
        parent[root_b] = root_a
        number[root_a] += number[root_b]


for _ in range(n):
    parent = dict()
    number = dict()
    F = int(input())
    for _ in range(F):
        a, b = input().split()
        if not a in parent:
            parent[a] = a
            number[a] = 1
        if not b in parent:
            parent[b] = b
            number[b] = 1
        union(a, b)
        print(number[find(a)])
