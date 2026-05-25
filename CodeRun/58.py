import sys
# input = lambda :sys.stdin.readline()[:-1]
ni = lambda :int(input())
na = lambda :list(map(int,input().split()))

yes = lambda :print('yes');Yes = lambda :print('Yes');YES = lambda : print('YES')
no = lambda :print('no');No = lambda :print('No');NO = lambda : print('NO')
#######################################################################


def solve(x, y, d, e):
    return (x <= d and y <= e) or (x <= e and y <= d)


def main():
# t = int(input())
# for _ in range(t):
#     solve()
    a, b, c, d, e = list(map(int, [input() for _ in range(5)]))

    if solve(a, b, d, e) or solve(a, c, d, e) or solve(b, c, d, e):
        print('YES')
    else:
        print('NO')


if __name__ == "__main__":
    main()
