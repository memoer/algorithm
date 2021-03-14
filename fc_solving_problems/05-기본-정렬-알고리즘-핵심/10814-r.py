n = int(input())
arr = []
for _ in range(n):
    age, name = input().split()
    arr.append((int(age), name))
arr.sort(key=lambda x: x[0])
for age, name in arr:
    print(f"{age} {name}")