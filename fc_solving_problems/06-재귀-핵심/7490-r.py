from copy import deepcopy


def solve(n: int, operations: list) -> None:
    if len(operations) == n:
        operations_list.append(deepcopy(operations))
        return
    operations.append(" ")
    solve(n, operations)
    operations.pop()

    operations.append("+")
    solve(n, operations)
    operations.pop()

    operations.append("-")
    solve(n, operations)
    operations.pop()


test_case = int(input())

for _ in range(test_case):
    n = int(input())
    operations_list = []
    solve(n - 1, [])
    for operations in operations_list:
        string = ""
        for i in range(1, n):
            string += str(i) + operations[i - 1]
        string += str(n)
        if eval(string.replace(" ", "")) == 0:
            print(string)
    print()
