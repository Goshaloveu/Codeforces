import sys

"""
8
6 3
WBWWWB
--> 2
7 3
WWBWBWW
--> 1
5 4
BWBWB
--> 2
5 5
BBBBB
--> 1
8 2
BWBWBBBB
--> 4
10 2
WBBWBBWBBW
--> 3
4 1
BBBB
--> 4
3 2
WWW
--> 0
"""

def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        s = list(input())
        cnt = 0

        for i in range(n):
            if s[i] == "B":
                for j in range(min(k, n-i)):
                    s[i + j] = "W"
                cnt += 1

        print(cnt)


if __name__ == "__main__":
    main()
