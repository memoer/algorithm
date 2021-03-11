# 1. 배열에 있는 모든 값을 검색
# 2. 가장 작은 값을 첫 번째로
# 3. 첫 번째 제외 배열 모든 값 검색
# 4. 가장 작은 값을 두 번째로
def swap(arr, a_idx, b_idx):
    arr[a_idx], arr[b_idx] = arr[b_idx], arr[a_idx]


def s_sort(arr: list) -> None:
    for i in range(len(arr) - 1):
        minum_idx = i
        for j in range(i + 1, len(arr)):
            if arr[minum_idx] > arr[j]:
                minum_idx = j
        if minum_idx != i:
            swap(arr, minum_idx, i)


arr = [
    3,
    6,
    2,
    1,
    7,
    5,
]

s_sort(arr)
print(arr)