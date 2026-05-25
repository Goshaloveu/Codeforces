import sys


def solve():
    n = int(input())
    a = list(map(int, input().split()))

    ls = [[] for i in range(4)]
    for i in a:
        if i % 2 == 0:
            if i % 3 == 0:
                ls[0].append(i)
            else:
                ls[1].append(i)
        elif i % 3 == 0:
            ls[2].append(i)
        else:
            ls[3].append(i)

    print(*ls[0], *ls[1], *ls[3], *ls[2])


def main():
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
