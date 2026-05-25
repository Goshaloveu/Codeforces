import sys

"""
5
R
RR
--> YES
LRLR
LRLR
--> YES
LR
LLLR
--> NO
LLLLLRL
LLLLRRLL
--> NO
LLRLRLRRL
LLLRLRRLLRRRL
--> YES
"""

def solve():
    a, b = input(), input()
    n, m = len(a), len(b)

    i = j = 0
    while i < n and j < m:
        c = a[i]
        if b[j] != c:
            print("NO")
            return

        lp = 0
        while i < n and a[i] == c:
            i += 1
            lp += 1

        ls = 0
        while j < m and b[j] == c:
            j += 1
            ls += 1

        if not (lp <= ls <= 2 * lp):
            print("NO")
            return

    print("YES" if i == n and j == m else "NO")


def main():
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
