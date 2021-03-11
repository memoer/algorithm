from time import time
from random import sample


def merge(left: list, right: list) -> list:
    """
n이 8이라면 -> 총 3단계의 depth가 생긴다 ( 맨 위의 root 를 제외하고 : 8 -> 4/4 -> 2/2/2/2 -> 1/1/1/1/1/1/1/1 )
1. 즉 log(2)n의 depth가 생기는 것 -> log(2)n

각 단계마다의 반복 횟수 -> 2^i * n/2^i
    -> 나눠진 함수의 갯수 * 리스트의 길이 -> 8의 2번째 깊이 ->  총 4개 나눠짐 / 리스트의 길이:2 -> 4 * 2 = 8
    -> n 이 8이라면 2번째 단계에서의 반복횟수 -> 4 * 8 / 4 -> 8
    -> n 이 8이라면 1번째 단계에서의 반복 횟수 -> 2 * 8 / 2 -> 8
2. 즉 n의 반복횟수

--> O(n) = nlog(2)n
"""
    merged = list()
    lp, rp = 0, 0
    # left, right 중에 item이 하나라도 남아있을 때
    while len(left) > lp and len(right) > rp:
        if left[lp] > right[rp]:
            merged.append(right[rp])
            rp += 1
        else:
            merged.append(left[lp])
            lp += 1
    # left에만 아이템이 남아 있을 때
    if len(left) > lp:
        merged += left[lp:]
    # right에만 아이템이 남아 있을 때
    if len(right) > rp:
        merged += right[rp:]
    return merged


def split(data: list) -> list:
    if len(data) <= 1:
        return data
    center_index = len(data) // 2
    return merge(split(data[:center_index]), split(data[center_index:]))


time_list = []
for _ in range(0, 100):
    data = sample(range(100), 10)
    start_time = time()
    split(data)
    process_time = time() - start_time
    time_list.append(process_time)

print(print(sum(time_list) / len(time_list)))
