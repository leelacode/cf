for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    f = True
    c = 0
    x = [a[i]-(i+1) for i in range(n)]
    for i in x:
        c += i
        if c < 0:
            f = False
    print(f and 'yes' or 'no')