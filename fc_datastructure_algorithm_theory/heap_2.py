import random


class ArrayUtility:
    def __init__(self, num: int or [int] or None = None) -> None:
        self.data = [None]
        if isinstance(num, list):
            self.data += num
        elif isinstance(num, int):
            self.data.append(num)

    def swap(self, a_idx, b_idx):
        self.data[a_idx], self.data[b_idx] = self.data[b_idx], self.data[a_idx]

    def data_exists(self, check_idx) -> bool:
        return len(self.data) - 1 >= check_idx


class Heap(ArrayUtility):
    def __init__(self, num: int or [int] or None = None) -> None:
        super().__init__(num)

    def push(self, num: int) -> None:
        self.data.append(num)
        cur_idx = len(self.data) - 1
        parent_idx = cur_idx // 2
        while cur_idx != 1:
            if self.data[cur_idx] <= self.data[parent_idx]:
                break
            else:
                self.swap(cur_idx, parent_idx)
                cur_idx = parent_idx
                parent_idx //= 2

    def get_higher_idx(self, a_idx, b_idx):
        return a_idx if self.data[a_idx] >= self.data[b_idx] else b_idx

    def pop(self) -> int:
        self.swap(1, len(self.data) - 1)
        return_value = self.data.pop()
        cur_idx = 1
        while True:
            left_child_idx = cur_idx * 2
            right_child_idx = left_child_idx + 1
            if self.data_exists(right_child_idx):
                higher_idx = self.get_higher_idx(left_child_idx, right_child_idx)
                if self.data[cur_idx] >= self.data[higher_idx]:
                    break
                self.swap(cur_idx, higher_idx)
                cur_idx = higher_idx
            elif self.data_exists(left_child_idx):
                if self.data[left_child_idx] <= self.data[cur_idx]:
                    break
                self.swap(cur_idx, left_child_idx)
                cur_idx = left_child_idx
            else:
                break
        return return_value


heap = Heap()
for i in range(0, 10):
    heap.push(random.randint(0, 100))
print(heap.data)
for i in range(0, 10):
    print(heap.pop())
