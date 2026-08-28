for _ in range(int(input())):
    n = int(input())
    a = [i for i in range(2, n+1)]
    a.append(1)
    print(*a)