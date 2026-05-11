import sys

"""
1 -> No
2 -> No
3 -> No
4 -> Yes
6 -> 2 + 4 -> Yes
"""

def main():
    n = int(input())
    print("YES" if (n % 2 == 0) and (n > 2) else "NO")


if __name__ == "__main__":
    main()
