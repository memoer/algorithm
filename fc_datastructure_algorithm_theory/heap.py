import random


class Heap:
    def __init__(self) -> None:
        self.tree = [None]

    def print(self) -> None:
        print(self.tree)

    def push(self, num: int) -> None:
        self.tree.append(num)
        parent_idx = len(self.tree) // 2
        cur_idx = len(self.tree) - 1
        while cur_idx != 1:
            if self.tree[parent_idx] < self.tree[cur_idx]:
                self.tree[parent_idx], self.tree[cur_idx] = (
                    self.tree[cur_idx],
                    self.tree[parent_idx],
                )
                cur_idx = parent_idx
                parent_idx //= 2
            else:
                break

    def get_root_node(self) -> int:
        self.tree[1], self.tree[-1] = self.tree[-1], self.tree[1]
        return self.tree.pop(-1)

    def over_idx_in_tree(self, idx) -> bool:
        if len(self.tree) - 1 < idx:
            return True
        return False

    def swap(self, a_idx, b_idx) -> None:
        self.tree[a_idx], self.tree[b_idx] = self.tree[b_idx], self.tree[a_idx]

    def pop(self) -> int:
        root_node = self.get_root_node()
        cur_idx = 1
        while True:
            left_child_idx = cur_idx * 2
            right_child_idx = left_child_idx + 1
            can_access_left_child = not self.over_idx_in_tree(left_child_idx)
            can_access_right_child = not self.over_idx_in_tree(right_child_idx)
            if not (can_access_right_child or can_access_left_child):
                break
            if can_access_right_child:
                left_child_node = self.tree[left_child_idx]
                right_child_node = self.tree[right_child_idx]
                if self.tree[cur_idx] < left_child_node and self.tree[cur_idx] < right_child_node:
                    higher_child_idx = (
                        left_child_idx if left_child_node > right_child_node else right_child_idx
                    )
                    self.swap(cur_idx, higher_child_idx)
                    cur_idx = higher_child_idx
                elif self.tree[cur_idx] < left_child_node:
                    self.swap(cur_idx, left_child_idx)
                    cur_idx = left_child_idx
                elif self.tree[cur_idx] < right_child_node:
                    self.swap(cur_idx, right_child_idx)
                    cur_idx = right_child_idx
                else:
                    break
            else:
                if self.tree[cur_idx] > self.tree[left_child_idx]:
                    break
                self.swap(cur_idx, left_child_idx)
                cur_idx = left_child_idx

        return root_node


heap = Heap()
for i in range(0, 10):
    heap.push(random.randint(1, 100))
heap.print()
for i in range(0, 10):
    print(heap.pop())

# 1. over (idx 계산 잘못함)
# 반복문 빠져나가는 거 생각 못함 ( 1번 변경되면 끝내야하는데, 안끝나지고 2번을 변경시켰음 )
