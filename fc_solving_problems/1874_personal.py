n = int(input())
stack = []
result = []
count = 1
for _ in range(n):
    data = int(input())
    while count <= data:
        stack.append(count)
        result.append("+")
        count += 1
    if stack[-1] == data:
        stack.pop()
        result.append("-")
    else:
        print("NO")
        exit(0)
print("\n".join(result))