import sys

"""
6
7
3 4 5 2 9 1 1
--> 3 1 4 1 5 9 2
4
9 2 7 1
--> 9 1 2 7
11
8 4 3 1 2 7 8 7 9 4 2
--> 8 2 4 4 3 9 1 7 2 8 7
1
42
--> 42
2
11 7
--> 11 7
8
1 1 1 1 1 1 1 1
--> 1 1 1 1 1 1 1 1
"""

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        b = list(map(int, input().split()))

        ans = [0] * n
        l, r = 0, n-1
        for i in range(n):
            if i % 2:
                ans[i] = b[r]
                r -= 1
            else:
                ans[i] = b[l]
                l += 1

        print(*ans)


if __name__ == "__main__":
    main()
