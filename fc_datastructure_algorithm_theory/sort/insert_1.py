from random import sample


def i_sort(list: list) -> list:
  """
   최선의 경우 -> (n-1)번만 루프를 돈다 -> O(n)
   최악의 경우 -> 외부 루프 안의 각 반복마다 i번의 비교 수행 -> n(n-1)/2 -> O(n^2)
   비교 [외부 루프만 생각] : [ n-1 ] 번 반복
  """
  for i in range(1, len(list)):
    target = list[i]
    if target > list[i-1]:
      continue
    """
    비교[내부 루프만 생각] : [1, 2, 3, ... (n-1)] 번 반복
    내부 루프를 모두 더하면 해당 함수의 모든 비교 횟수가 되므로
    ->∑(k-1) = n(n+1)/2 - n
    ->n(n-1)/2
    ->O(n ^ 2)
    """
    while i > 0 and list[i-1] > target:
      list[i] = list[i-1]
      i -= 1
    list[i] = target


list = sample(range(100), 20)
i_sort(list)
print(list)
