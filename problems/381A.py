import sys

"""
4
4 1 2 10
--> 12 5

7
1 2 3 4 5 6 7
--> 16 12
"""

def main():
    n = int(input())
    ls = list(map(int, input().split()))

    user = [0, 0]
    r, l = 0, -1
    for i in range(n):
        if ls[r] > ls[l]:
            user[i % 2] += ls[r]
            r += 1
        else:
            user[i % 2] += ls[l]
            l -= 1

    print(*user)


if __name__ == "__main__":
    main()
