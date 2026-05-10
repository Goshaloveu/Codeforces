import sys


"""
chr(ord(i) | 32) -- converts any (lower/upper) letter to lowercase
chr(ord(i) & ~32) -- converts any letter to uppercase

Codeforces
--> .c.d.f.r.c.s
"""

def main():
    ls = ["A", "O", "Y", "E", "U", "I"]
    s = list(input())
    res = []

    for i in s:
        if chr(ord(i) & ~32) in ls:
            continue
        res.append('.' + chr(ord(i) | 32))

    print("".join(res))


if __name__ == "__main__":
    main()
