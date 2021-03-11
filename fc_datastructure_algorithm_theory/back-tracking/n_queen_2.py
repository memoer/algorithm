# 이해!
def is_available(candidate, current_col):
    current_row = len(candidate)
    for queen_row in range(current_row):
        # candidate[queen_row] == current_col -> 같은 열 체크
        #
        # abs(candidate[queen_row] - current_col) -> 퀸이 배치되어 있는 열과 다음으로 배치할 열의 간격
        # current_row - queen_row -> 퀸이 존재하는 행과 다음으로 배치할 행의 간격
        # 두 간격이 같다면 대각선이므로 퀸 배치 불가
        if (
            candidate[queen_row] == current_col
            or abs(candidate[queen_row] - current_col) == current_row - queen_row
        ):
            return False
    return True


def DFS(N, current_row, current_candidate, final_result):
    if current_row == N:
        final_result.append(current_candidate[:])
        print(final_result)
        return

    for candidate_col in range(N):
        if is_available(current_candidate, candidate_col):
            current_candidate.append(candidate_col)
            DFS(N, current_row + 1, current_candidate, final_result)
            # print(current_candidate)
            current_candidate.pop()


def solve_n_queens(N):
    final_result = []
    DFS(N, 0, [], final_result)
    return final_result


solve_n_queens(4)