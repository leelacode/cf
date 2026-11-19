t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    a = [0]*n
    scan = []
    for i in range(n):
        if s[i] == '1':
            scan.append(i)
        elif s[i] == '2':
            if scan:
                a[scan.pop()] = 1
            else:
                a[i] = 1
        else:
            a[i] = 1
    x = [i+1 for i in range(n) if a[i] == 0]
    print(len(x))
    print(*x)