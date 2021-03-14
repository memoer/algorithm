n, m = list(map(int, input().split(" ")))
data = list(map(int, input().split(" ")))
result = 0


for i in range(0, n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            sum_value = data[i] + data[j] + data[k]
            if sum_value <= m:
                result = max(result, sum_value)

print(result)