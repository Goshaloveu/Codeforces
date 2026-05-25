import sys

"""
fast way to check zeros in list - any(res)
fast way to sum lists - [x + y for x, y in zip(a, b)]

3
3 -1 7
-5 2 -4
2 -1 -3
--> YES

3
4 1 7
-2 4 -1
1 -5 -3
--> NO
"""

def main():
    n = int(input())
    res = [0] * 3
    for _ in range(n):
        res  = [x + y for x, y in zip(res, map(int, input().split()))]

    print("NO" if any(res) else "YES")


if __name__ == "__main__":
    main()
