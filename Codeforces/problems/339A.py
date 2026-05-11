import sys

"""
3+2+1
--> 1+2+3
2
--> 2
"""

def main():
    n = sorted(list(map(int, input().split('+'))))
    # print(n)
    print('+'.join(map(str, n)))


if __name__ == "__main__":
    main()
