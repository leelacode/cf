for _ in range(int(input())):
    a = list(map(int, input().split()))
    if (a[0] != a[1] != a[2]):
        a.sort()
        print(min(a[2]-a[1], a[1]-a[0]))
    else:
        print(0)