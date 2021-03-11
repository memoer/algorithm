'''
2. 부분 배낭 문제
 - 무게 제한이 k인 배낭에 최대 가지를 가지도록 물건을 넣는 문제
 - 물건은 쪼개질 수 있으므로, 물건의 일부분이 배낭에 넣어질 수 있음
'''
# (무게, 가치)
item_list = [(25, 8), (10, 10), (15, 12), (20, 10), (30, 5)]


def insert(item_list: list, max_capacity: int) -> (list, int):
  # 무게 대비 가치가 가장 큰 것이 맨 앞에 위치
  item_list.sort(reverse=True, key=lambda item: item[1]/item[0])
  inserted_item_list = list()
  total_worth = 0
  cur_capacity = 0
  for item in item_list:
    weight = item[0]
    worth = item[1]
    # 현재 가방의 무게가 max_capacity미만이라면
    if cur_capacity < max_capacity:
      # 현재 가방에 아이템 전체를 넣을 수 있는 공간이 있다면
      if cur_capacity + weight <= max_capacity:
        inserted_item_list.append(item)
        cur_capacity += weight
        total_worth += worth
      # 그렇지 않다면 나눈다.
      else:
        rest_capacity = max_capacity - cur_capacity
        cal_worth = worth / weight * rest_capacity
        inserted_item_list.append((rest_capacity, cal_worth))
        cur_capacity += rest_capacity
        total_worth += cal_worth
    # 현재 가방의 무게가 max_capacity와 이상이라면
    else:
      break
  return inserted_item_list, total_worth


print(insert(item_list, 60))
