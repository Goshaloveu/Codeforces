import sys


"""
4
abacaba
acaba
abacaba
acab
-->
OK
OK
abacaba1
OK

6
first
first
second
second
third
third
-->
OK
first1
OK
second1
OK
third1

"""

def main():
    n = int(input())
    x = set()
    ls = {}
    for i in range(n):
        tmp = input()
        if tmp not in x:
            print('OK')
            x.add(tmp)
            ls[tmp] = 0
        else:
            print(tmp + str(ls[tmp] + 1))
            ls[tmp] += 1


if __name__ == "__main__":
    main()
