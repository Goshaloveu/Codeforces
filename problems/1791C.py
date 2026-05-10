import sys

"""
3
100
--> 1

4
0111
--> 
"""

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()

        r, l = 0, -1
        while (r < (n + l)) and ((int(s[r]) + int(s[l])) == 1):
            r += 1
            l -= 1

        print(0 if r > (n + l) else (n + l + 1) - r)


if __name__ == "__main__":
    main()
