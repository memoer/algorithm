# 수 정렬하기 3
# 계수정렬이용
import sys

n = int(input())
temp = [0] * 10001

for _ in range(n):
    temp[int(sys.stdin.readline())] += 1
for i in range(len(temp)):
    for _ in range(temp[i]):
        print(i)
