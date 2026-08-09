for _ in range(int(input())):
    n = int(input())
    f = 0
    s = input()
    for i in range(10, 0, -1):
        if '#'*i in s:
            f = i
            break
    print((f+1)//2)