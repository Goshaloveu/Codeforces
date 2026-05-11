import sys


def main():
    s = input()
    f = ord(s[0])
    if f < 97:
        print(s)
    else:
        print(chr(ord(s[0]) - 32) + s[1:])

if __name__ == "__main__":
    main()
