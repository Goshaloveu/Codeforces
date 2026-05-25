import sys

"""
4
1 2 4 6
5
1 5 5 7 9
--> 3

4
6 7 8 9
5
1 2 3 3 3
--> 0

2
2 1
2
2 3
--> 2
"""

def main():
    cnta = [0] * 102
    cntb = [0] * 102

    n = int(input())
    for i in map(int, input().split()):
        cnta[i] += 1

    m = int(input())
    for i in map(int, input().split()):
        cntb[i] += 1

    a, b = [], []
    for i in range(1, 101):
        a.extend([i] * cnta[i])
        b.extend([i] * cntb[i])

    i = j = cnt = 0
    while i < n and j < m:
        if abs(a[i] - b[j]) <= 1:
            cnt += 1
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1

    print(cnt)


if __name__ == "__main__":
    main()
