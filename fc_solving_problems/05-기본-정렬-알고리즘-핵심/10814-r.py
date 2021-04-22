n = int(input())
data = list()

for _ in range(n):
    age, name = input().split()
    data.append((int(age), name))
data.sort(key=lambda x: x[0])
for age, name in data:
    print(age, name)