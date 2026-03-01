def lower_bound(a, x):
    l, r = 0, len(a)
    while l < r:
        m = (l + r) // 2
        if a[m] < x:
            l = m + 1
        else:
            r = m
    return l


def upper_bound(a, x):
    l, r = 0, len(a)
    while l < r:
        m = (l + r) // 2
        if a[m] <= x:
            l = m + 1
        else:
            r = m
    return l


def solve() -> None:
    n = int(input().strip())
    nums = list(map(int, input().split()))
    target = int(input().strip())
    first = lower_bound(nums, target)
    if first == n or nums[first] != target:
        print(f"Element {target} is not found in the array")
        return

    last = upper_bound(nums, target) - 1
    print(f"The first occurrence of element {target} is located at index {first}")
    print(f"The last occurrence of element {target} is located at index {last}")


if __name__ == "__main__":
    solve()
