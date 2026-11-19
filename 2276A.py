t = int(input())
for _ in range(t):
    c, s = map(int, input().split())
    if c <= s:
        print(-1)
    else:
        c = c-s
        if c <= s:
            print(c)
        else:
            print(s)