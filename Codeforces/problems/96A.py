import sys


def solve():
    pass


def main():
    prv = ''
    cnt = 0
    res = False
    for i in input():
        if i == prv:
            cnt += 1
        else:
            prv = i
            cnt = 0
        if cnt == 6:
            res = True
    print('YES' if res else "NO")


if __name__ == "__main__":
    main()
