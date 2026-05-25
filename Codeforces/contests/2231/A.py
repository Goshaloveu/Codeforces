import sys


def solve():
    n = int(input())

    if n == 1:
        print(1)
        return
    if n == 2:
        print(1, 2)
        return

    c = 0
    res = []
    cnt = 0
    while cnt < n:
        if c % 3 != 0:
            res.append(c)
            cnt += 1
        c += 1

    print(*res)


def main():
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
