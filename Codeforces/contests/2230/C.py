import sys


def solve():
    n = int(input())
    ls = list(map(int, input().split()))

    tmp = sum(x > 1 for x in ls)
    if tmp == 0:
        print(0)
        return

    inch = n - tmp
    res = 0
    for i in ls:
        if i >= 2:
            res += i
            if (i >= 4) or (tmp == 1):
                c = min(i // 2 if (tmp == 1) else (i // 2) - 1, inch)
                inch -= c
                res += c

    if res < 3:
        print(0)
        return
    print(res)


def main():
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
