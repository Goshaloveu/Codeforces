import sys
# input = lambda :sys.stdin.readline()[:-1]
ni = lambda :int(input())
na = lambda :list(map(int,input().split()))

yes = lambda :print('yes');Yes = lambda :print('Yes');YES = lambda : print('YES')
no = lambda :print('no');No = lambda :print('No');NO = lambda : print('NO')
#######################################################################


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    for i in range(n):
        if a[i] > b[i]:
            a[i], b[i] = b[i], a[i]

    print(max(a) + sum(b))


def main():
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
