import sys

"""
4
5
0 -1 3 -3 0
5
0 -2 1 2 3
5
0 1 0 1 0
2
1000000000 -1000000000
-->
3
5
4
1
"""

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        tmp = list(map(int, input().split()))
        ans = 0
        for i in range(n-1, -1, -1):
            if tmp[i] > 0:
                ans += 1
                tmp[i-1] += tmp[i]
        print(ans)


if __name__ == "__main__":
    main()
