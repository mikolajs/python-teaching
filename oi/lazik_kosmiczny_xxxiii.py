import math

def createTab(n, m):
    tab = []
    for i in range(n):
        tab.append(['o']*m)
    return tab

def drawTab(tab):
    for t in tab:
        print(''.join(t))

def checkIfAll(tab):
    for line in tab:
        for z in line:
            if z == 'o':
                return False
    return True

def mkMove(move, tab):
    R = len(tab)
    K = len(tab[0])
    r, c = 0, 0
    tab[r][c] = 'x'
    S = 10000 
    for i in range(S):
        for k in move:
            if k == 'G':
                r -= 1
                if r < 0:
                    r = R - 1
            elif k == 'D':
                r += 1
                if r >= R:
                    r = 0
            elif k == 'L':
                c -= 1
                if c < 0:
                    c = K - 1
            elif k == 'P':
                c += 1
                if c >= K:
                    c = 0
            else:
                print('błędny znak', k)
            tab[r][c] = 'x'
            #print(k, r, c)
            #drawTab(tab)
        #print('dodane', r, c)


move = ['PD', 'DP', 'PPD', 'DDP', 'PPPD', 'DDDP', 'DDPP', 'PPDD', 'DDDDP' ]


def test():
    N, M = 4, 4
    stat = {}
    for i in range(2, 5):
        stat[i] = []
    for i in range(2, 50):
        N = i
        for j in range(2, 50):
            M = j
            tab = createTab(N,M)
            ss = False
            for m in move:
                mkMove(m, tab)
              #if N == 4 and M == 4:
                #    print(m#)
                #    drawTab(tab)
                if checkIfAll(tab):
                    ss = True
                    if (N, M) not in stat[len(m)]:
                        stat[len(m)].append((N, M))
                    break

            if not ss:
                print(N, M, math.gcd(N, M), "porażka")
                #drawTab(tab)

def test2():
    N, M = 4, 4
    stat = {}
    for i in range(2, 50):
        N = i
        for j in range(2, 50):
            M = j
            tab = createTab(N,M)
            ss = False
            for m in move:
                mkMove(m, tab)
                if checkIfAll(tab):
                    ss = True
                    r = math.gcd(N, M)

                    if m not in stat:
                        stat[m] = set()
                        stat[m].add( r)
                    else:
                        stat[m].add( r)
    
            if not ss:
                print("nieudane", N, M, math.gcd(N, M))
    for m, tab in stat.items():
        print(m, list(tab))

test2()
#tab = createTab(4, 4)
#mkMove(move[2], tab)

