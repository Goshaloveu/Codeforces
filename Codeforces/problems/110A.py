import sys


def main():
    n = map(int, list(input()))

    print("YES" if sum(1 for i in n if i in (4, 7)) in (4, 7) else "NO")


if __name__ == "__main__":
    main()
