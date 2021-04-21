# N-Queen
# 각 행/열에는 하나의 퀸만 올 수 있음
# 퀸이 놓아진 칸에 대하여 대각선의 칸에는 다른 퀸을 놓을 수 없음


def is_available(candidate: list, col: int) -> bool:
    cur_row = len(candidate)
    for row in range(cur_row):
        already_replaced_col = candidate[row]
        if col == already_replaced_col or cur_row - row == abs(col - already_replaced_col):
            return False
    return True


def DFS(n: int, candidate: list):
    if len(candidate) == n:
        return [candidate[:]]
    result = []
    for col in range(n):
        if is_available(candidate, col):
            candidate.append(col)
            answer = DFS(n, candidate)
            candidate.pop()
            result.extend(answer)
    return result


print(DFS(4, []))