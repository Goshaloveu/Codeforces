import sys


def solve():
    s = input()
    new = [i for i in s if i != '4']
    n = len(new)

    if n == 0:
        print(len(s))
        return

    ss = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        ss[i] = ss[i + 1] + (1 if new[i] in {'1', '3'} else 0)

    ps = 0
    bs = ss[0]
    for i in range(n):
        if new[i] == '2':
            ps += 1
        bs = max(bs, ps + ss[i + 1])

    print(len(s) - bs)


def main():
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
