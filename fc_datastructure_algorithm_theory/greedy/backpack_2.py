from functools import reduce


def get_max_value(capacity):
    # weight/value
    data_list = sorted(
        [(10, 10), (15, 12), (20, 10), (25, 8), (30, 5)], key=lambda data: data[0] / data[1]
    )
    inserted_data = []
    for data in data_list:
        if capacity == 0:
            break
        exceed_capacity = True if capacity > data[0] else False
        fraction = 1 if exceed_capacity else capacity / data[0]
        capacity = capacity - data[0] if exceed_capacity else 0
        inserted_data.append([data[0], data[1], fraction])
    return (
        inserted_data,
        reduce(
            lambda pre, cur: pre + cur, [value * fraction for (_, value, fraction) in inserted_data]
        ),
    )


print(get_max_value(30))

