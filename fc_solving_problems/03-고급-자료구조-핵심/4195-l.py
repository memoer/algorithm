test_case = int(input())


def find(x):
    if parent[x] == x:
        return x
    else:
        root = find(parent[x])
        parent[x] = root
        return root


def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x != root_y:
        parent[root_x] = root_y
        number[root_y] += number[root_x]


for _ in range(test_case):
    parent = dict()
    number = dict()
    f = int(input())
    for _ in range(f):
        x, y = list(input().split())
        if not x in parent:
            parent[x] = x
            number[x] = 1
        if not y in parent:
            parent[y] = y
            number[y] = 1
        union(x, y)
        print(number[find(y)])
