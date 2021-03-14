a, b = 0, 1
n = int(input())
while n - 1 > 0:
    a, b = b, a + b
    n -= 1
print(b)