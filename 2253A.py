from math import isqrt

for _ in range(int(input())):
    n = int(input()) + 1
    f = True
    if n < 2:
        f = False
    else:
        for i in range(2, isqrt(n) + 1):
            if n % i == 0:
                f = False
                break
    print("YES" if f else "NO")