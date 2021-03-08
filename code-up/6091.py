# 6091
from functools import reduce

l = list(map(int, input().split()))
t = []
while not all(val == 1 for val in l):
    m = min(list(filter(lambda x: x != 1, l)))
    t.append(m)
    l = [k // m if k % m == 0 else k for k in l]
mul = reduce(lambda pre, cur: pre * cur, t)
print(mul)