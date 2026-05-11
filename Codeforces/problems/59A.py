import sys

"""
HoUse            
--> house
"""

def main():
    s = input()
    u, l = 0, 0
    for i in map(ord, s):
        if i < 91:
            u += 1
        else:
            l += 1
    if u > l:
        res = [chr(ord(i) & ~32) for i in s]
    else:
        res = [chr(ord(i) | 32) for i in s]
    print(''.join(res))


if __name__ == "__main__":
    main()
