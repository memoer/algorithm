# key-logger
# 강의
n = int(input())
for _ in range(n):
    case = input()
    l_stack = []
    r_stack = []
    for i in case:
        if i == "<":
            if len(l_stack) != 0:
                r_stack.append(l_stack.pop())
        elif i == ">":
            if len(r_stack) != 0:
                l_stack.append(r_stack.pop())
        elif i == "-":
            if len(l_stack) != 0:
                l_stack.pop()
        else:
            l_stack.append(i)
    l_stack.extend(reversed(r_stack))
    print("".join(l_stack))
