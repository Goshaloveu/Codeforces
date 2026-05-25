import sys
from collections import Counter

def solve():
    pass


def main():
    n = input()
    s = Counter(input())

    print('Anton' if s['A'] > s['D'] else 'Danik' if s['A'] < s['D'] else 'Friendship')


if __name__ == "__main__":
    main()
