string = input()
a = []
for s in string:
    a.append(int(s))
a.sort(reverse=True)
print("".join(map(str, a)))
