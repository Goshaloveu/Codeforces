import sys


def main():
    n, k = map(int, input().split())
    cnt = 0
    while n <= k:
        cnt +=1 
        n *= 3
        k *= 2

    print(cnt)


if __name__ == "__main__":
    main()
