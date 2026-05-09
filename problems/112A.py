import sys


def main():
    f, s = input(), input()
    
    for i in range(len(f)):
        a, b = ord(f[i]), ord(s[i])
        if abs(a - b) in (0, 32):
            continue
        if a > 96:
            a -= 32
        if b > 96:
            b -= 32
        
        if a < b:
            print(-1)
            return
        else:
            print(1)
            return
    print(0)


if __name__ == "__main__":
    main()
