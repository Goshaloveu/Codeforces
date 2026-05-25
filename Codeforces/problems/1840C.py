import sys

"""
7
3 1 15
-5 0 -10
--> 
"""

def main():
    t = int(input())
    for _ in range(t):
        n, k, q = map(int, input().split())
        ls = list(map(int, input().split()))

        res = 0
        cnt = 0
        for i in range(n + 1):
            if (i == n) or ls[i] > q:
                if cnt >= k:
                    for i in range(k, cnt + 1):
                        res += cnt - i + 1
                cnt = 0
                continue
            cnt += 1
        print(res)


if __name__ == "__main__":
    main()
