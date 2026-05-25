import sys
# input = lambda :sys.stdin.readline()[:-1]
ni = lambda :int(input())
na = lambda :list(map(int,input().split()))

yes = lambda :print('yes');Yes = lambda :print('Yes');YES = lambda : print('YES')
no = lambda :print('no');No = lambda :print('No');NO = lambda : print('NO')
#######################################################################


def solve():
    pass


def main():
# t = int(input())
# for _ in range(t):
#     solve()
    n, m = map(int, input().split())
    ls = [list(map(int, input().split())) for _ in range(n)]

    dp1 = [[-1] * (m) for _ in range(n)]
    dp1[0][0] = ls[0][0]

    for i in range(1, m):
        dp1[0][i] = dp1[0][i-1] + ls[0][i]
    for i in range(1, n):
        dp1[i][0] = dp1[i-1][0] + ls[i][0]
    # print('=' * 10)
    # print(*dp1[0])
    for i in range(1, n):
        for j in range(1, m):
            dp1[i][j] = min(dp1[i-1][j], dp1[i][j-1]) + ls[i][j]
        # print(*dp1[i])

    print(dp1[-1][-1])


if __name__ == "__main__":
    main()
