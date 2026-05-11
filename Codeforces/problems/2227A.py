import sys

"""
6
1 1
--> NO
1 2
--> YES
4 6
--> YES
5 9
--> NO
7 2
--> YES
10 10
--> YES
"""

def main():
    t = int(input())
    for _ in range(t):
        x, y = map(int, input().split())
        even = (x % 2) + (y % 2)
        print('NO' if even > 1 else 'YES')


if __name__ == "__main__":
    main()
