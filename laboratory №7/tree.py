def solve() -> None:
    n = int(input().strip())
    if n == 0:
        print(0)
        return
    left = [None] * n
    right = [None] * n
    for _ in range(n):
        parts = input().split()
        idx = int(parts[0])
        ltok = parts[2]
        rtok = parts[3]
        left[idx] = None if ltok == "None" else int(ltok)
        right[idx] = None if rtok == "None" else int(rtok)
    stack = [(0, 1)]
    ans = 0
    while stack:
        v, d = stack.pop()
        if d > ans:
            ans = d
        lv = left[v]
        rv = right[v]
        if lv is not None:
            stack.append((lv, d + 1))
        if rv is not None:
            stack.append((rv, d + 1))
    print(ans)


if __name__ == "__main__":
    solve()
