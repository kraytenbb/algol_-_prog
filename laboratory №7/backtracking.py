def solve() -> None:
    n = int(input().strip())

    cols = set()
    diag1 = set()
    diag2 = set()

    pos = [-1] * n 
    solutions = []

    def backtrack(row: int) -> None:
        if row == n:
            board = []
            for r in range(n):
                line = ['.'] * n
                line[pos[r]] = 'Q'
                board.append(''.join(line))
            solutions.append(board)
            return
        for col in range(n):
            d1 = row - col
            d2 = row + col
            if col in cols or d1 in diag1 or d2 in diag2:
                continue

            pos[row] = col
            cols.add(col)
            diag1.add(d1)
            diag2.add(d2)
            backtrack(row + 1)
            cols.remove(col)
            diag1.remove(d1)
            diag2.remove(d2)
            pos[row] = -1
    backtrack(0)

    if not solutions:
        print("[]")
        return

    for si, board in enumerate(solutions):
        print("[", end="")
        for i, row in enumerate(board):
            if i < n - 1:
                print(f'"{row}",\n', end="")
            else:
                print(f'"{row}"', end="")
        print("]")

        if si != len(solutions) - 1:
            print()

if __name__ == "__main__":
    solve()
