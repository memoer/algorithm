# 직접 구현
# https://www.acmicpc.net/problem/2920 - 음계
arr = list(map(int, input().split()))
tmp = arr[0]
msg = ""
for i in range(1, len(arr)):
    if tmp + 1 == arr[i]:
        if i + 1 == len(arr):
            msg = "ascending"
        else:
            tmp += 1
    elif tmp - 1 == arr[i]:
        if i + 1 == len(arr):
            msg = "descending"
        else:
            tmp -= 1
    else:
        is_mixed = True
        msg = "mixed"
        break
print(msg)
