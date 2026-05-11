import sys

"""

"""

def main():
    n = int(input())
    a = list(map(int, input().split()))
    pos = {4: 0, 8: 1, 15: 2, 16: 3, 23: 4, 42: 5}
    ls = [0] * 6

    for i in a:
        if pos[i] > 0 and ls[pos[i]-1] > 0:
            ls[pos[i]-1] -= 1
            ls[pos[i]] += 1
        if pos[i] == 0:
            ls[0] += 1

    print(n - 6 * ls[-1])


if __name__ == "__main__":
    main()
