import sys


def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    for i in range(q):
        tmp = int(input()) - 1
        if tmp == (n - 1):
            a[tmp] = 0
            continue
        a[tmp + 1] += a[tmp]
        a[tmp] = 0

    print(*a)


if __name__ == "__main__":
    main()
