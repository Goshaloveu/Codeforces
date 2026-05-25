import sys


def solve():
    pass


def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())

        print("YES" if (n % 2 + k % 2) <= 1 else "NO")


if __name__ == "__main__":
    main()
