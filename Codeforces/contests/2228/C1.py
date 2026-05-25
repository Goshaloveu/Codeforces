import sys


def solve():
    a, n = map(str, input().split())
    ai = int(a)
    al = len(a)
    d = list(map(int, input().split()))

    low = ''
    res = []
    for i, x in enumerate(a):
        c = int(x)
        cl = (i == 0 and al > 1)
        cnc = [j for j in d if j <= c and (j > 0 or not cl)]
        if not cnc:
            fn = False
            while res:
                pr = res.pop()
                ps = len(res)
                v = [j for j in d if j < pr and (j > 0 or not (ps == 0 and al > 1))]
                if v:
                    res.append(max(v))
                    res += [d[1]] * (al - len(res))
                    fn = True
                    break
            low = ''.join(map(str, res)) if fn else ''
            break
        bs = max(cnc)
        res.append(bs)
        if bs < c:
            res += [d[1]] * (al - len(res))
            low = ''.join(map(str, res))
            break
    if not low:
        low = ''.join(map(str, res))

    upp = ''
    res = []
    for i, x in enumerate(a):
        c = int(x)
        cl = (i == 0 and al > 1)
        cnc = [j for j in d if j >= c and (j > 0 or not cl)]
        if not cnc:
            fn = False
            while res:
                pr = res.pop()
                ps = len(res)
                v = [j for j in d if j > pr and (j > 0 or not (ps == 0 and al > 1))]
                if v:
                    res.append(min(v))
                    res += [d[0]] * (al - len(res))
                    fn = True
                    break
            upp = ''.join(map(str, res)) if fn else ''
            break
        bs = min(cnc)
        res.append(bs)
        if bs > c:
            res += [d[0]] * (al - len(res))
            upp = ''.join(map(str, res))
            break
    if not upp:
        upp = ''.join(map(str, res))

    ans = float('inf')
    if low:
        ans = min(ans, ai - int(low))
    if upp:
        ans = min(ans, int(upp) - ai)

    if al > 1:
        ans = min(ans, ai - int(str(d[1]) * (al - 1)))

    fr = d[1] if d[0] == 0 else d[0]
    ans = min(ans, int(str(fr) + str(d[0]) * al) - ai)

    print(ans)


def main():
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
