import sys


def solve():
    n = int(input())
    k = list(map(int, input().split()))

    tmpd = {}
    for i in range(n):
        tmpd[i] = [-1, -1]

    for i in range(len(k)):
        if tmpd[k[i]][0] == -1:
            tmpd[k[i]][0] = i
        else:
            tmpd[k[i]][1] = i

    cent = {}
    for x, y in tmpd.items():
        c = round((y[0] + y[1]) / 2, 2)
        if cent.get(c):
            cent[c].append((y[1], x))
        else:
            cent[c] = [(y[1], x)]

    res = [1]
    for x, y in cent.items():
        y = sorted(y, key=lambda x: x[0])
        l = (int(x), k[int(x)])
        mex = {l[1]}
        for a in y:
            if a[0] != (l[0] + 1):
                break
            l = a
            mex.add(l[1])
        m = 0
        while m in mex:
            m += 1
        res.append(m)

    print(max(res))


def main():
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
