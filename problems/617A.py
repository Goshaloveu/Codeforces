import sys


def main():
    n = int(input())
    ls = [5, 4, 3, 2, 1]

    cnt = 0
    for i in range(5):
        cnt += n // ls[i]
        n %= ls[i]

    print(cnt)


if __name__ == "__main__":
    main()
