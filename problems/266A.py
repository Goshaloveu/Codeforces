import sys

"""
5
RRRRR
--> 4
4
BRBG
--> 0
10
BBBRRRGGGR
"""

def main():
    n = int(input())
    s = input()

    cnt = 0
    for i in range(n-1):
        if s[i] == s[i+1]:
            cnt += 1

    print(cnt)


if __name__ == "__main__":
    main()
