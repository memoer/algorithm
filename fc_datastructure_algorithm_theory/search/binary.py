# 이진탐색
from random import sample


def binary_search(data: list, to_search_number: int) -> int:
  # n /2 /2 /2 /2 /2 ..... -> 1이 될 때까지 반복 -> k 번 반복 ( 마지막 배열의 개수가 1이 될 때까지 반복한다는 것. )
  # n /2^(k) = 1 -> n = 2^(k) -> log(2)n = k
  # O(n) = log(2)n
  if len(data) == 1:
    if data[0] == to_search_number:
      return True
    else:
      return False
  center_idx = len(data)//2
  if data[center_idx] > to_search_number:
    return binary_search(data[:center_idx], to_search_number)
  else:
    return binary_search(data[center_idx:], to_search_number)


sample_data = sorted(sample(range(20), 10))

print(sample_data)
print(binary_search(sample_data, 8))
