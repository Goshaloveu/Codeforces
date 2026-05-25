import sys


def solve():
    n, x1, x2, k = map(int, input().split())

    print(k + min(abs(x1-x2), n - abs(x1 - x2)) if n > 3 else 1)


def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
