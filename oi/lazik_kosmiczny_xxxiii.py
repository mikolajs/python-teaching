
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
    N = len(tab)
    M = len(tab[0])
    r, c = 0, 0
    S = 20000
    for i in range(S):
        for k in move:
            if k == 'G':
                r -= 1
                if r < 0:
                    r = N-1
            elif k == 'D':
                r += 1
                if r >= N:
                    r = 0
            elif k == 'L':
                c -= 1
                if c < 0:
                    c = M -1
            elif k == 'P':
                c += 1
                if c >= M:
                    c = 0
            else:
                print('błędny znak', k)
            tab[r][c] = 'x'
        #print('dodane', r, c)


move = ['PD', 'PPD', 'PDD']
N, M = 4, 4
for i in range(2, 20):
    N = i
    for j in range(2, 20):
        M = j
        tab = createTab(N,M)
        ss = False
        for m in move:
            mkMove(m, tab)
        #drawTab(tab)
            if checkIfAll(tab):
                ss = True

        if not ss:
            print(N, M, "porażka")
            #drawTab(tab)
