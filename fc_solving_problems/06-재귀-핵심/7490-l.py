from copy import deepcopy

test_case = int(input())


def recursive(array: list, n: int) -> None:
    if len(array) == n:
        opertions_list.append(deepcopy(array))
        return

    array.append(" ")
    recursive(array, n)
    array.pop()

    array.append("+")
    recursive(array, n)
    array.pop()

    array.append("-")
    recursive(array, n)
    array.pop()


for _ in range(test_case):
    n = int(input())
    num_list = [i for i in range(1, n + 1)]
    opertions_list = []
    recursive([], n - 1)
    for opertions in opertions_list:
        string = ""
        for i in range(len(num_list) - 1):
            string += str(num_list[i]) + opertions[i]
        string += str(num_list[-1])
        if eval(string.replace(" ", "")) == 0:
            print(string)
    print()