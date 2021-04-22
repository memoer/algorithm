n = int(input())
for _ in range(n):
    data = input()
    l_stack = list()
    r_stack = list()
    for i in data:
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
    r_stack.reverse()
    print("".join(l_stack + r_stack))
