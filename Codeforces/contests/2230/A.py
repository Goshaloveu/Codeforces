import sys


def solve():
    n, a, b = map(int, input().split())

    res = [0, 0]
    if b <= (a * 3):
        res[1] += n // 3
        n %= 3
    else:
        res[0] += (n // 3) * 3
        n %= 3
    if b <= (a * n):
        res[1] += 1
    else:
        res[0] += n

    print(res[0] * a + res[1] * b)


def main():
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
