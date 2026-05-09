import sys


def main():
    n = int(input())
    ls = list(map(int, input().split()))
    prz = list(map(int, input().split()))
    ans = [0] * 5

    sm = 0
    i = 0
    while i <= n:
        while sm >= prz[0]:
            for j in range(4, -1, -1):
                if sm >= prz[j]:
                    tmp = sm // prz[j]
                    sm -= tmp * prz[j]
                    ans[j] += tmp
                    break
        if i < n:
            sm += ls[i]
        i += 1
    print(*ans)
    print(sm)


if __name__ == "__main__":
    main()
