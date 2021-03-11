from functools import reduce

# (capacity, value)
data_list = [(10, 10), (15, 12), (20, 10), (25, 8), (30, 5)]


def get_max_value(data_list: list, capacity: int) -> list:
    sorted_data_list_by_value = sorted(data_list, key=lambda data: data[1] / data[0], reverse=True)
    pushed_data_to_back_pack = []
    for data in sorted_data_list_by_value:
        if capacity == 0:
            break
        elif capacity < data[0]:
            value_per_capacity = data[1] / data[0]
            pushed_data_to_back_pack.append((capacity, capacity * value_per_capacity))
            capacity -= capacity
        else:
            pushed_data_to_back_pack.append(data)
            capacity -= data[0]
    return pushed_data_to_back_pack


back_pack = get_max_value(data_list, 30)
all_values = reduce(lambda pre, cur: pre + cur, [data[1] for data in back_pack])
print(all_values)
