arr = list(map(int, list(input())))
arr.sort(reverse=True)
print("".join(map(str, arr)))
