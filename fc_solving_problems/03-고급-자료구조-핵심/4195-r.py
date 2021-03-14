def find(x: str) -> str:
    if x == parent[x]:
        return x
    else:
        root = find(parent[x])
        parent[x] = root
        return root


def union(x: str, y: str):
    root_x = find(x)
    root_y = find(y)
    if root_x != root_y:
        parent[root_x] = root_y
        count[root_y] += count[root_x]


n = int(input())
for _ in range(n):
    parent = dict()
    count = dict()
    f = int(input())
    for _ in range(f):
        x, y = input().split()
        if not x in parent:
            parent[x] = x
            count[x] = 1
        if not y in parent:
            parent[y] = y
            count[y] = 1
        union(x, y)
        print(count[find(y)])
