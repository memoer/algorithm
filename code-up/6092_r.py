n = int(input())
d = [0 for _ in range(0, 24)]
i = list(map(int, input().split()))

for j in i:
    d[j] += 1
print(" ".join(map(str, d[1:])))