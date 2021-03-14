import sys

n = int(input())
counting = [0] * 10001
for _ in range(n):
    counting[int(sys.stdin.readline())] += 1
for i in range(len(counting)):
    for _ in range(counting[i]):
        print(i)
