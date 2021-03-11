def binary_search(arr: list, num: int, previous_idx: int) -> int:
    center = len(arr) // 2
    if arr[center] == num:
        return previous_idx + center
    elif len(arr) == 1:
        return previous_idx if arr[0] == num else -1
    isGreater = arr[center] < num
    i = arr[center:] if isGreater else arr[:center]
    j = previous_idx + (center if isGreater else 0)
    return binary_search(i, num, j)