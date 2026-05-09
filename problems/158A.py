import sys

"""
8 5
10 9 8 7 7 7 5 5
--> 6 (participant at 7th place scored the same num of points)
4 2
0 0 0 0
--> 0 (nobody scored positive num of points)
"""

def main():
    n, k = map(int, input().split())

    ans = 0
    bord = 0

    for i, x in enumerate(map(int, input().split()), start=1):
        if i == k:
            bord = x

        if x > 0 and x >= bord:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
