import sys


def solve():
    pass


def main():
    n, m = map(int, input().split())
    dp = [list(map(int, input().split())) for _ in range(n)]
    dp1 = [[''] * m for _ in range(n)]
    dp2 = [[-1] * m for _ in range(n)]
    dp2[0][0] = dp[0][0]

    for i in range(1, m):
        dp2[0][i] = dp[0][i] + dp2[0][i-1]
        dp1[0][i] = 'R'

    for i in range(1, n):
        dp2[i][0] = dp[i][0] + dp2[i-1][0]
        dp1[i][0] = 'D'

    for i in range(1, n):
        for j in range(1, m):
            if dp2[i-1][j] > dp2[i][j-1]:
                dp2[i][j] = dp2[i-1][j] + dp[i][j]
                dp1[i][j] = 'D'
            else:
                dp2[i][j] = dp2[i][j-1] + dp[i][j]
                dp1[i][j] = 'R'

    # for i in range(n):
    #     print(*dp1[i])

    res = []
    x, y = m-1, n-1
    while x or y:
        # print(x, y)
        nx = dp1[y][x]
        res.append(nx)
        if nx == 'D':
            y -= 1
        else:
            x -= 1

    print(dp2[-1][-1])
    print(*res[::-1])


if __name__ == "__main__":
    main()
