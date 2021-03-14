# 복습
num_list = list(map(int, input().split()))

ascending = False
descending = False

for i in range(1, len(num_list)):
    if num_list[i - 1] < num_list[i]:
        ascending = True
    else:
        descending = True
    if ascending and descending:
        print("mixed")
        break
if not (ascending and descending):
    print("ascending" if ascending else "descending")
