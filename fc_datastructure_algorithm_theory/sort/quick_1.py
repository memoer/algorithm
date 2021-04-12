from random import sample


def q_sort(data: list) -> list:
    print(data)
    if len(data) <= 1:
        return data

    left, right = list(), list()
    pivot = data[0]

    for i in range(1, len(data)):
        if pivot > data[i]:
            left.append(data[i])
        else:
            right.append(data[i])
    print(f"pivot\t: {pivot}")
    print(f"left\t: {left}")
    print(f"right\t: {right}")
    print("------------------")
    return q_sort(left) + [pivot] + q_sort(right)


def q_sort_comp(data: list) -> list:
    """
  pivot을 기준으로 양 옆이 반반일 때 -> 가장 평균적인 형태

  평균 -> O(nlog(n))
  최악 -> O(n^2)
  """
    if len(data) <= 1:
        return data
    pivot = data[0]
    left = [item for item in data[1:] if pivot > item]
    right = [item for item in data[1:] if pivot <= item]
    return q_sort_comp(left) + [pivot] + q_sort_comp(right)


sample_data = sample(range(20), 10)
# print(q_sort(sample_data))
print(q_sort_comp(sample_data))
