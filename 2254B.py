for _ in range(int(input())):
    n = int(input())
    s = input().strip() + '0'
    l = []
    c = 1
    x = s[0]
    for i in range(1, n+1):
        if s[i] == x:
            c += 1
        else:
            l.append((x, c))
            c = 1
            x = s[i]
    k = len(l)
    ans = k
    for i in range(1, k-1):
        if l[i][1] == 1:
            if l[i-1][0] == l[i+1][0]:
                ans = k - 2
                break
            ans = k - 1
    print(ans)