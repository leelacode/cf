from collections import Counter

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    count = Counter(a)

    x, m = count.most_common(1)[0]
    other = n - m

    if m <= other + 1:
        print(sum(a))
    else:
        print(sum(a) - (m - (other + 1)) * x)