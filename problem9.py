# problem9
from operator import itemgetter
import copy
import sys

def facs(n):
    fac = [] 
    for i in range(1, n + 1):
        if n % i == 0:
            fac.append(i)
            continue
        else:
            pass
    return fac

def ptyprint(list_set):
    print(list_set)

trans = [set(facs(i)) for i in range(1, 101)]

# L1
def Lyr1():
    L1 = []
    count = [0] * 101
    for i in trans:
        for j in i:
            count[j] = count[j] + 1
    for i, j in enumerate(count):
        if j >= 5:
            L1.append(i)
    return L1

# L2
def Lyr2(L1):
    L2 = []
    cands = []
    for i, j in enumerate(L1):
        for k in L1[i+1:]:
            cands.append(set((j, k)))
    for i in cands:
        tmp = 0
        for j in trans:
            if i < j:
                tmp = tmp + 1
        if tmp >= 5:
            L2.append(i)
    return L2


def Lyrn(n: int, Lyr2: list, Lyr1: list) -> list:
    if n < 3:
        return []
    Lyr = 3
    Ln = []
    Lprev = copy.deepcopy(Lyr2)
    while Lyr <= n:
        Ln = []
        cands = []
        # 產生候選組合
        for i in Lprev:
            for j in Lyr1:
                if j not in i:
                    k = i.copy()
                    k.add(j)
                    if k not in cands:
                        cands.append(k)
        # 挑選真正的 frequency
        for i in cands:
            tmp = 0
            for j in trans:
                if i < j:
                    tmp = tmp + 1
            if tmp >= 5:
                Ln.append(i)
        Lyr = Lyr + 1
        Lprev = Ln
    return Ln

if __name__=='__main__':
    if (len(sys.argv) < 2) or (2 < len(sys.argv)):
        print('error number of parameter!')
    elif sys.argv[1] == '1':
        print(Lyr1())
    elif sys.argv[1] == '2':
        print(Lyr2(Lyr1()))
    else:
        print(Lyrn(int(sys.argv[1]), Lyr2(Lyr1()), Lyr1()))
