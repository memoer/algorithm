# 직접 구현해본 것
class NQueen:
    def get_board(self, N: int) -> list:
        board = []
        for i in range(N):
            temp = []
            for j in range(N):
                temp.append((i, j))
            board.append(temp)
        return board

    def solved_board(self, N: int) -> list:
        board = self.get_board(N)
        result = []
        for location_x in board[0]:
            x, y = location_x
            temp = [location_x]
            no = list(
                set(
                    filter(
                        lambda tu: tu[1] >= 0,
                        [(x + 1, y - 1), (x + 1, y), (x + 1, y + 1)]
                        + [(x + k, y) for k in range(N)],
                    )
                )
            )
            for location_list_y in board[1:]:
                for location_y in location_list_y:
                    appended = False
                    if location_y not in no:
                        i, j = location_y
                        temp.append(location_y)
                        appended = True
                        no += list(
                            set(
                                filter(
                                    lambda tu: tu[1] >= 0,
                                    [
                                        (i + 1, j - 1),
                                        (i + 1, j),
                                        (i + 1, j + 1),
                                    ]
                                    + [(i + k, j) for k in range(N)],
                                )
                            )
                        )
                        break
                if not appended:
                    break
                if len(temp) == N:
                    result.append(temp)
        return result


n_queen = NQueen()
print(n_queen.solved_board(5))