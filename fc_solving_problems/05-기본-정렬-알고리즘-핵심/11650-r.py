n = int(input())
result = []
for _ in range(n):
    x, y = input().split()
    result.append((int(x), int(y)))
result.sort(key=lambda x: (x[0], x[1]))
for x, y in result:
    print(x, y)
