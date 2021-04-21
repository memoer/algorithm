n = int(input())
stack = []
result = []
last_num = 0


def add(n: int):
    stack.append(n)
    result.append("+")


def pop():
    stack.pop()
    result.append("-")


for _ in range(n):
    m = int(input())
    if m > last_num:
        for i in range(last_num + 1, m + 1):
            add(i)
        last_num = i
    if stack[-1] == m:
        pop()
    else:
        print("NO")
        exit(0)

print("\n".join(result))