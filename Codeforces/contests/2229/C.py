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

    res = []
    t = 0
    for i in range(n-1, -1, -1):
        if (a[i] * (-1) ** t) > 0:
            res.append(i)
            t ^= 1

    print(len(res))
    print(*[i + 1 for i in res])


def main():
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
