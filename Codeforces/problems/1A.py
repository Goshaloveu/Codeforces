import sys

"""
6 6 4
--> 4 (2 pieces by X and 2 pieces by Y)

Math formula for dividing the whole with rounding up:
result = (a + b - 1) // b
"""


def main():
    n, m, a = map(int, input().split())
    print((int((n + a - 1) // a) * ((m + a - 1) // a)))


if __name__ == "__main__":
    main()
