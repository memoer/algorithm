# 피보나치
# DP 이용
n = int(input())
a, b = 0, 1

while n - 1 > 0:
    a, b = b, a + b
    n -= 1

print(b)