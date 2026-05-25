import sys


def solve():
    x = int(input())
    if x < 1400:
        print('Division 4')
        return
    if x < 1600:
        print('Division 3')
        return
    if x < 1900:
        print("Division 2")
        return
    print("Division 1")


def main():
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
