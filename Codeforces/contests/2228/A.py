import sys


def solve():
    n = int(input())
    w = list(map(int, input().split()))

    res = 0
    cnt = {0: 0, 1: 0, 2: 0}
    for i in range(n):
        cnt[w[i]] += 1
    
    if cnt[0]:
        res += cnt[0]
        cnt[0] = 0
    if (cnt[1] > 0) and (cnt[2] > 0):
        tmp = min(cnt[1], cnt[2])
        res += tmp
        cnt[1] -= tmp
        cnt[2] -= tmp
    if cnt[2] >= 3:
        tmp = cnt[2] // 3
        cnt[2] -= tmp * 3
        res += tmp
    if cnt[1] >= 3:
        tmp = cnt[1] // 3
        cnt[1] -= tmp * 3
        res += tmp

    print(res)


def main():
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
