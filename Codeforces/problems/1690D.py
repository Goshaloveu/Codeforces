import sys

"""
4
5 3
BBWBW
--> 1
5 5
BBWBW
--> 2
5 1
BBWBW
--> 0
1 1
W
--> 1
"""

def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        s = input()

        cnt = l = 0
        res = k
        for i in range(n):
            if s[i] == "W":
                cnt += 1
            if (i - l + 1) > k:
                if s[l] == "W":
                    cnt -= 1
                l += 1
            if (i - l + 1) == k:
                res = min(res, cnt)

        print(res)


if __name__ == "__main__":
    main()
