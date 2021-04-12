def find(x: str) -> str:
    if parent[x] == x:
        return parent[x]
    else:
        root_x = find(parent[x])
        parent[x] = root_x
        return root_x


def union(x: str, y: str):
    root_x = find(x)
    root_y = find(y)
    if root_x != root_y:
        parent[root_x] = root_y
        count[root_y] += count[root_x]


for _ in range(int(input())):
    count, parent = dict(), dict()
    for _ in range(int(input())):
        x, y = input().split()
        if not x in parent:
            parent[x] = x
            count[x] = 1
        if not y in parent:
            parent[y] = y
            count[y] = 1
        union(x, y)
        print(count[find(y)])
