import sys


def main():
    n, t = map(int, input().split())
    ls = list(map(int, input().split()))

    res, tmp = 0, 0
    l = 0
    for r in range(n):
        tmp += ls[r]
        while tmp > t:
            tmp -= ls[l]
            l += 1
        res = max(res, r - l + 1)

    print(res)


if __name__ == "__main__":
    main()
