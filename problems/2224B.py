import sys


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        ls = sorted(list(map(int, input().split())))

        new = [ls[-1]]
        seen = set(new)
        tmp = []
        for i in range(0, n-1):
            if ls[i] in seen:
                tmp.append(ls[i])
                continue
            new.append(ls[i])
            seen.add(ls[i])
        new = new + tmp
        ax, ex = new[0] * n, 0
        exs = set()
        cur = 0
        for i in range(0, n):
            exs.add(new[i])
            while cur in exs:
                cur += 1
            ex += cur
        print(ax + ex)


if __name__ == "__main__":
    main()
