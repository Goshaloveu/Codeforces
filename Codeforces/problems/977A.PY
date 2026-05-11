import sys

"""
512 4
--> 50

1000000000 9
--> 1
"""

def main():
    n, k = map(int, input().split())
    for _ in range(k):
        if n % 10 == 0:
            n //= 10
        else:
            n -= 1
    print(n)


if __name__ == "__main__":
    main()
