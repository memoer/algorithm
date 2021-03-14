# 복습
n = int(input())
count = 1
stack = []
result = []
for _ in range(n):
    data = int(input())
    while data >= count:
        stack.append(count)
        count += 1
        result.append("+")
    if data == stack[-1]:
        stack.pop()
        result.append("-")
    else:
        print("NO")
        exit(0)
print("\n".join(result))