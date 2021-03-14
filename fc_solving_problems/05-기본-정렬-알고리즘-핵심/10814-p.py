n = int(input())

result = {}
for _ in range(n):
    age, name = input().split()
    if age in result.keys():
        result[age].append(f"{age} {name}")
    else:
        result[age] = [f"{age} {name}"]

users_order_by_age = sorted(result.items(), key=lambda x: int(x[0]))
str_list = map(lambda x: "\n".join(x[1]), users_order_by_age)
print("\n".join(str_list))
