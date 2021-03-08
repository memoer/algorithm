n = int(input())
l = []
for i in range(n):
    k = tuple(map(int, input().split()))
    l.append(k)

for i in range(1, 20):
    for j in range(1, 20):
        u = (i, j)
        matched = u in l
        print("1" if matched else "0", end=" ")
    print("")
