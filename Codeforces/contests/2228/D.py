import sys
from array import array


def main():
    buf = sys.stdin.buffer.read()
    pos = 0
    nb = len(buf)

    def rd():
        nonlocal pos
        while pos < nb and buf[pos] < 48:
            pos += 1
        v = 0
        while pos < nb and buf[pos] >= 48:
            v = v * 10 + buf[pos] - 48
            pos += 1
        return v

    t = rd()
    out = []

    for _ in range(t):
        n = rd()
        S = n + 1

        enc = []
        for _ in range(n):
            enc.append(rd() * S + rd())
        enc.sort()

        gmin = array('i')
        gmax = array('i')
        i = 0
        while i < n:
            v = enc[i]
            cx = v // S
            mn = mx = v % S
            i += 1
            while i < n and enc[i] // S == cx:
                y = enc[i] % S
                if y < mn:
                    mn = y
                elif y > mx:
                    mx = y
                i += 1
            gmin.append(mn)
            gmax.append(mx)

        m = len(gmin)
        if m < 2:
            out.append(0)
            continue

        pmin = array('i', gmin)
        pmax = array('i', gmax)
        for i in range(1, m):
            if pmin[i-1] < pmin[i]:
                pmin[i] = pmin[i-1]
            if pmax[i-1] > pmax[i]:
                pmax[i] = pmax[i-1]

        smin = array('i', gmin)
        smax = array('i', gmax)
        for i in range(m-2, -1, -1):
            if smin[i+1] < smin[i]:
                smin[i] = smin[i+1]
            if smax[i+1] > smax[i]:
                smax[i] = smax[i+1]

        seen = bytearray(n + 1)
        for v in enc:
            seen[v % S] = 1

        yr = array('i', [0] * (n + 1))
        c = 0
        for v in range(1, n + 1):
            if seen[v]:
                yr[v] = c
                c += 1

        ans = 0
        for i in range(m - 1):
            lo = yr[pmin[i]]
            lo2 = yr[smin[i+1]]
            if lo2 > lo:
                lo = lo2
            hi = yr[pmax[i]]
            hi2 = yr[smax[i+1]]
            if hi2 < hi:
                hi = hi2
            hi -= 1
            if hi >= lo:
                ans += hi - lo + 1

        out.append(ans)

    sys.stdout.write('\n'.join(map(str, out)))


if __name__ == "__main__":
    main()
