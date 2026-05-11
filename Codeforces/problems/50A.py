import sys

"""
2 4
--> 4
3 3
--> 4
"""

def main():
    m, n = map(int, input().split())

    ans = (m // 2) * n
    if m % 2 != 0:
        ans += n // 2

    print(ans)


if __name__ == "__main__":
    main()
