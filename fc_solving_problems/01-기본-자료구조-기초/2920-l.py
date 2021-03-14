# 강의용
# https://www.acmicpc.net/problem/2920 - 음계

arr = list(map(int, input().split()))
ascending = True
descending = True
for i in range(1, len(arr)):
    if arr[i] > arr[i - 1]:
        # 한 번 만이라도, 커진다면 descending은 아니니까
        descending = False
    else:
        ascending = False

if ascending:
    print("ascending")
elif descending:
    print("descending")
else:
    print("mixed")
