import sys


def solve():
    n = int(input())
    ls = list(map(int, input().split()))

    def pth(x):
        res = {}
        o = 0
        sn = set()

        while x not in sn:
            sn.add(x)
            res[x] = o
            if x % 2 == 0:
                x //= 2
            else:
                x += 1
            o += 1
        return res

    m = min(ls)
    trg = list(pth(m).keys())
    pths = [pth(i) for i in ls]

    ans = float('inf')
    for i in trg:
        tot = 0
        val = True
        for j in pths:
            c = j.get(i, -1)
            if c == -1:
                val = False
                break
            tot += c
        if val:
            ans = min(ans, tot)

    print(ans)


def main():
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
