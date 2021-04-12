import random


def b_sort(list: list) -> list:
    # 기본정렬
    arr_length = len(list)
    print(f"Start : {list}")
    for i in range(arr_length - 1):
        print("------------------------------")
        print(f">> Number : {i + 1}")
        swap = False
        # (n-1) + (n-2) + (n-3) + ... 1 -> n(n-1)/2
        # 시간 복잡도 = O(n^2)
        for j in range(arr_length - 1 - i):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                swap = True
                print(f"change : {list}")
        # swap 이 false 라는 것은 이미 정렬된 배열이기 때문에
        # 반복문을 돌리지 않고 바로 나간다.
        if swap == False:
            break
    return list


# 0 ~ 100 의 사이에서 50개
tmp = random.sample(range(100), 20)
print(b_sort(tmp))
