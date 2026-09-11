
N = 4550
P = 850
i = 1
while N > P:
    print(i, round(P, 1), round(N, 1), round(N/P, 2))
    N *= 1.01
    P *= 1.037
    i += 1


