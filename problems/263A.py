import sys

"""
0 0 0 0 0
0 0 0 0 1
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
--> 3

0 0 0 0 0
0 0 0 0 0
0 1 0 0 0
0 0 0 0 0
0 0 0 0 0
--> 3
"""

def main():
    x = (0, 0)
    for i in range(5):
        tmp = input().split()
        for j in range(5):
            if tmp[j] == "1":
                x = (i + 1, j + 1)
    print(abs(x[0] - 3) + abs(3 - x[1]))


if __name__ == "__main__":
    main()
