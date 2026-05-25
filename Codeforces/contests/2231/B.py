import sys


def solve():
    n = int(input())
    ls = list(map(int, input().split()))

    dsc = [i for i in range(n-1) if ls[i] > ls[i+1]]

    if not dsc:
        print('YES')
        return

    for i in range(len(dsc) - 1):
        if dsc[i + 1] == dsc[i] + 1:
            print('NO')
            return

    mn = max(ls[i] - ls[i + 1] for i in dsc)

    res = float('inf')
    for i in range(len(dsc) - 1):
        l = dsc[i] + 1
        r = dsc[i + 1]
        mx = max(ls[j + 1] - ls[j] for j in range(l, r))
        res = min(res, mx)

    print('YES' if mn <= res else 'NO')


def main():
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
