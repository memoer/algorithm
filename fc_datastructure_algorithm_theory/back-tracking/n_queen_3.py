def is_available(current_col: int, candidate_col: list) -> bool:
    current_row = len(candidate_col)
    for previous_row in range(current_row):
        if (
            candidate_col[previous_row] == current_col
            or abs(candidate_col[previous_row] - current_col) == current_row - previous_row
        ):
            return False
    return True


def DFS(N: int, current_row: int, candidate_col: list, result: list):
    if current_row == N:
        # 만약, current_row가 N과 같다면 candidate_col에 4개의 값을 가진 배열이 존재한다는 것.
        # current_row -> 0부터 시작함 -> 0,1,2,3,4...
        print(candidate_col)
        # 깊은 복사!!
        result.append(candidate_col[:])
        return
    # 이 for문이 열을 검사하는 것.
    # 즉, 4행 -> DFS 4번 호출됨
    # 4열 -> DFS내부에서 for문이 4번 호출
    for current_col in range(N):
        if is_available(current_col, candidate_col):
            candidate_col.append(current_col)
            # DFS함수 자체가 row(행)을 검사하는 것과 마찬가지
            DFS(N, current_row + 1, candidate_col, result)
            # 3번째 행까지 검사 진행 후, 4번째 행 검사에서 4개의 열에 대한 (DFS내부 for문)이 모두 is_available이 아니였다면
            # 4번째 행 검사의 DFS가 끝나고 -> 3번째 행에 대한 열 candidate_col을 빼낸다 -> 왜냐하면 4번째 행에 적합한 열이 존재하지 않기 때문
            # 3번째 행에 대한 열 candidate_col을 뺴내고, 다음 열 (for문)을 검사
            # 적합(is_available) 하다면, candidate_col.append -> DFS -> current_row>N으로 인해 result.append
            # 그 다음, 모두 끝났으니, 마지막 행에 대한 열 (candidate_col) 제거
            # 다시 그 뒤의 행(3번째 행)의 DFS로 돌아가서 for문 호출
            candidate_col.pop()


def n_queen(N: int) -> list:
    result = []
    DFS(N, 0, [], result)
    return result


board = n_queen(4)
print(board)