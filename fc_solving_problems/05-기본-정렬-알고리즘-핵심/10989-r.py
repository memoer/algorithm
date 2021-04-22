import sys

n = int(input())
counting = [0] * 10001
for _ in range(n):
    n = int(sys.stdin.readline())
    counting[n] += 1
for idx, count in enumerate(counting):
    for i in range(count):
        print(idx)
