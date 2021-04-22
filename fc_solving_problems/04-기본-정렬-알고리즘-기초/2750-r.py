n = int(input())
data = []
for _ in range(n):
    j = int(input())
    data.append(j)
data.sort()
print("\n".join(map(str, data)))
