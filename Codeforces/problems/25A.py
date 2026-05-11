import sys

"""
5
2 4 7 8 10
--> 3 (more even nums)

4
1 2 1 1
--> 2 (more odd nums)
"""

def main():
    n = int(input())
    ls = [i % 2 for i in map(int, input().split())]
    
    if sum(ls[:3]) > 1:
        for i in range(1, n + 1):
            if ls[i-1] == 0:
                print(i)
                break
    else:
        for i in range(1, n + 1):
            if ls[i-1] == 1:
                print(i)
                break


if __name__ == "__main__":
    main()
