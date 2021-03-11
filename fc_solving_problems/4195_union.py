def find(x):
    if parent[x] == x:
        return parent[x]
    else:
        # path compression
        root = find(parent[x])
        parent[x] = root
        return root


def union(x, y):
    root_x = find(x)
    root_y = find(y)
    # union
    parent[root_y] = root_x


parent = []
for i in range(0, 5):
    parent.append(i)

union(1, 4)
union(2, 4)

for i in range(1, len(parent)):
    print(find(i), end=" ")
