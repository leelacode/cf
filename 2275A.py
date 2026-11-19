for t in range(int(input())):
    x, y, r = map(int, input().split())
    print(*[x+r, y])