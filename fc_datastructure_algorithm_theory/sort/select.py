import random


def s_sort(list: list) -> list:
  # 기본정렬
  smallest_idx = -1
  print(f'Start : {list}')
  for i in range(len(list) - 1):
    print('------------------------------')
    print(f'>> Number : {i + 1}')
    smallest_idx = i
    for j in range(i+1, len(list)):
      if list[smallest_idx] > list[j]:
        smallest_idx = j
    if smallest_idx != i:
      list[i], list[smallest_idx] = list[smallest_idx], list[i]
      print(f'Change : {list}')
  return list


list = random.sample(range(100), 10)
s_sort(list)
