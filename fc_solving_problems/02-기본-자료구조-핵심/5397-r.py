# 복습
n = int(input())
for _ in range(n):
    row_data = input()
    l_stack = []
    r_stack = []
    for one_data in row_data:
        if one_data == "<":
            if len(l_stack) > 0:
                r_stack.append(l_stack.pop())
        elif one_data == ">":
            if len(r_stack) > 0:
                l_stack.append(r_stack.pop())
        elif one_data == "-":
            if len(l_stack) > 0:
                l_stack.pop()
        else:
            l_stack.append(one_data)
    l_stack.extend(reversed(r_stack))
    print("".join(l_stack))
