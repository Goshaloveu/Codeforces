import sys


def solve():
    n = int(input())
    s = input()

    op = cl = 0
    for i in s:
        if i == "(":
            op += 1
        else:
            cl += 1

    print("YES" if op == cl else "NO")

def main():
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
