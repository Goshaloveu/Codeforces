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

    cn = sum([1 for _ in a if _ > 0])
    if cn == 0:
        print('0\n')
        return

    pos = neg = 0
    res = []
    for i in range(n):
        print(i)
        if a[i] > 0:
            pos += a[i]
        else:
            neg -= a[i]
        print(pos, neg)
        if (pos < neg or cn > 1) and (a[i] > 0):
            cn -= 1
            res.append(i + 1)
            pos, neg = neg, pos

    print(len(res))
    print(*res)


def main():
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
