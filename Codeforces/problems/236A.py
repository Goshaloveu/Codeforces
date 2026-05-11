import sys


def main():
    n = set(input())
    print("CHAT WITH HER!" if (len(n) % 2) == 0 else "IGNORE HIM!")


if __name__ == "__main__":
    main()
