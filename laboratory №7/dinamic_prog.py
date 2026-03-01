def solve() -> None:
    n = int(input().strip())
    a = [int(input().strip()) for _ in range(n)]
    INF = 10**18
    prev = [INF] * (n + 2)
    prev[0] = 0
    choices = [bytearray(n + 2) for _ in range(n + 1)]
    for i in range(1, n + 1):
        c = a[i - 1]
        bonus = 1 if c > 500 else 0
        curr = [INF] * (n + 2)
        ch_row = choices[i]

        for j in range(0, n + 1):

            pj = j - bonus
            if pj >= 0:
                cand = prev[pj] + c
                if cand < curr[j]:
                    curr[j] = cand
                    ch_row[j] = 0

            if j + 1 <= n:
                cand = prev[j + 1]
                if cand < curr[j]:
                    curr[j] = cand
                    ch_row[j] = 1
        prev = curr
    best_cost = min(prev[:n + 1])
    j = prev.index(best_cost)

    used_days = []
    for i in range(n, 0, -1):
        c = a[i - 1]
        bonus = 1 if c > 500 else 0
        if choices[i][j] == 1:
            used_days.append(i)
            j += 1
        else:
            j -= bonus
    used_days.reverse()
    print(best_cost, len(used_days))
    if used_days:
        print(*used_days)
    else:
        print()


if __name__ == "__main__":
    solve()
