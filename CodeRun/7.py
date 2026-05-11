import sys


def main():
    n, m = map(int, input().split())
    ls = {i: set() for i in range(1, n+1)}
    us = set()
    for i in range(m):
        x, y = map(int, input().split())
        ls[x].add(y)
        ls[y].add(x)
    
    def dfs(v):
        us.add(v)
        nd = set()
        nd.add(v)
        res = False
        if v == 1:
            res = True
        for i in ls[v]:
            nd.add(i)
            if i not in us:
                ans, tmp_nd = dfs(i)
                if ans:
                    res = ans
                nd = nd | tmp_nd
        return res, nd

    for i in ls.keys():
        if i not in us:
            ans, nd = dfs(i)
            if ans:
                print(len(nd))
                print(*sorted(nd))
                return
    print(0)
    return


if __name__ == "__main__":
    main()
