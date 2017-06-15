from pprint import pprint
from math import ceil
from math import exp
from sortedcontainers import SortedDict

import os


def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]


def readfile(file):
    readline = [line.strip() for line in open(file, 'r')]
    print("-------------------Time table", file[5:-4], "------------------")
    for line in readline:
        print(line)
    print("-----------------------------------------------")
    readline = [readline[i].split(", ") for i in range(len(readline))]
    minute = []
    hour = []
    troley = []
    for i in range(len(readline)):
        troley.append(readline[i][0][:3])
        readline[i][0] = readline[i][0][readline[i][0].index(' ') + 1:]
        minute.append([])
        hour.append([])

        for j in range(len(readline[i])):
            minute[i].append(int(readline[i][j][3:]))
            hour[i].append(int(readline[i][j][:2]))

    return hour, minute, troley


def min_convert():
    pre = []
    for i in range(len(Minute)):
        pre.append([])
        for j in range(len(Minute[i])):
            pre[i].append(Minute[i][j])

    for i in range(len(Minute)):
        j = 1
        k = 0
        while j < len(Minute[i]):
            if Hour[i][j] > Hour[i][j - 1]:
                k += 1
                Minute[i][j] += 60 * k

            if Minute[i][j] < Minute[i][j - 1]:
                Minute[i][j] += (60 * k)
            j += 1
    return pre


def gaps(H, M):
    y = []
    for i in range(len(M)):
        y.append([])
        for j in range(len(M[i])):
            if j + 1 != len(M[i]):
                if int(H[i][j]) < int(H[i][j + 1]):
                    y[i].append([int(M[i][j + 1]) - int(M[i][j]) + 60])
                else:
                    y[i].append([int(M[i][j + 1]) - int(M[i][j])])
    return y


def stats():
    val = 0
    for i in range(len(Hour)):
        val += len(Hour[i])
    print("Nr of trolley=", val)
    print("Pre Hours")
    pprint(Hour)
    print("Pre Minutes")
    pprint(Pre_Minute)
    print("Minutes from 11:00")
    pprint(Minute)
    print("Gaps")
    pprint(Gaps)


def extractGap(all):
    k = 1
    gap = []
    while k < len(all):
        gap.append(all[k] - all[k - 1])
        k += 1
    return gap


def optimize():
    all = []  # all minutes
    tall = []  # trolley
    for i in range(len(Minute)):
        for j in range(len(Minute[i])):
            all.append(Minute[i][j])
            tall.append(i)
    print("==================================")
    print("•Index all:", tall)
    print("•Time all:", all)
    all1 = all
    # memorise all indexes sorted
    allind = sorted(range(len(all)), key=lambda k: all[k])
    all = sorted(all)
    tall2 = [tall[allind[i]] for i in range(len(tall))]
    print("○Index all sorted:", tall2)
    print("○Time all sorted", all)
    gap = extractGap(all)
    print("GAP before=", gap)
    print("•Total Gap before", sum(gap), "\n•Average gap before=", sum(gap) / len(gap))
    print("==================================")
    # print("Indexes=", tall2,len(tall2))
    sgap = sum(gap)

    # print("All Gaps=", gap,len(gap))
    def something(x):
        for j in range(x):
            typed = []
            # print("•Total Gap before", sum(gap), "\n•Coef=",exp(sum(gap)/len(gap)))
            for i in range(len(gap)):
                if exp(gap[i]) <= exp(sum(gap) / len(gap)):
                    typed.append("+")
                else:
                    typed.append("-")

            if len(Hour)!=1:
                for a in range(len(typed)):
                    # print(gap[a], "<==", typed[a], tall2[a], a, gap)
                    if typed[a] == "+":
                        gap[a] += 1
                    if typed[a] == "-":
                        gap[a] -= 1
            if sgap <= sum(gap):
                for i in range(len(gap)):
                    if gap[i] == max(gap) and min(gap)==max(gap):
                        gap[i] -= 1
                    if sgap <= sum(gap):
                        if gap[i] == max(gap):
                            gap[i] -= 1
        return typed


                        # print("Stuff=",typed)

    typed=something(100)
    for i in range(len(gap)):
        gap[i] = int(gap[i])
    for i in range(len(all)):

             all[i] = all[i]+gap[i - 1]



    print("GAP after=", gap)
    print("•Total gap after=", sum(gap), "\n•Average gap after=", sum(gap) / len(gap))
    print(all)
    # print(tall2)
    Minute2 = [[] for i in range(len(Minute))]
    for i in range(len(tall2)):
        Minute2[tall2[i]].append(all[i])

    timelast = [[] for i in range(len(Minute2))]
    x = [[] for i in range(len(Minute2))]
    print("Minutes from 11:00")
    pprint(Minute2)
    for i in range(len(Minute2)):
        for j in range(len(Minute2[i])):
            y = 11
            for k in range(100):
                if Minute2[i][j] >= 60:
                    Minute2[i][j] = Minute2[i][j] - 60
                    y += 1
            x[i].append(y)

    for i in range(len(Minute2)):
        for j in range(len(Minute2[i])):
            if Minute2[i][j] < 10:
                timelast[i].append(str(x[i][j]) + ":0" + str(Minute2[i][j]))
            else:
                timelast[i].append(str(x[i][j]) + ":" + str(Minute2[i][j]))

    # pprint(x)
    # pprint(Minute2)
    # print("Optimized time table")
    # pprint(timelast)
    return timelast


def results(o, t):
    opt = []
    for i in range(len(o)):
        opt.append([t[i]])
        for j in range(len(o[i])):
            opt[i][0] += ' '
            opt[i][0] += o[i][j]
    print("Optimized time table")
    pprint(opt)


file = listdir_fullpath('txts')
for i in range(len(file)):
    print("\n■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■\n")
    Hour, Minute, Troley = readfile(file[i])
    Gaps = gaps(Hour, Minute)
    Pre_Minute = min_convert()
    # stats()
    optim = optimize()
    results(optim, Troley)
