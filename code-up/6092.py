n = int(input())
a = list(map(int, input().split()))
d = [str(a.count(i)) for i in range(1, 24)]

print(" ".join(d))
