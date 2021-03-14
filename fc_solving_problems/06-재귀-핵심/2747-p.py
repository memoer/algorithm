# 피보나치
n = int(input())
temp = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]
for i in range(len(temp), n + 1):
    temp.append(temp[i - 2] + temp[i - 1])
print(temp[n])
