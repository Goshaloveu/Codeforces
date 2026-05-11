import sys


def main():
    n = int(input())
    for i in range(n):
        tmp = input()
        if len(tmp) > 10:
            print("".join([tmp[0], str(len(tmp) - 2), tmp[-1]]))
        else:
            print(tmp)

if __name__ == "__main__":
    main()
