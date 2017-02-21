# Name: John David Brawn
# Email: jdbrawn@bu.edu
# Course: COMPSCI 320

import sys
import networkx

#with open('sample.txt') as f:
#    lines = f.readlines()
lines = sys.stdin.readlines()


counter = 1
for i in range(int(lines[0])):
    n, m = lines[counter].split()
    n = int(n)
    m = int(m)
    counter += 1
    difficulties = lines[counter].split()
    counter += 1
    types = lines[counter].split()
    counter += 1

    G = networkx.DiGraph()
    nodeCounter = 1

    # Sort into dictionaries and keep track of how many we need
    difficultiesDict = {}
    for dif in difficulties:
        try:
            difficultiesDict[dif][1] += 1
        except:
            difficultiesDict[dif] = [nodeCounter, 1]
            nodeCounter += 1

    typesDict = {}
    for typ in types:
        try:
            typesDict[typ][1] += 1
        except:
            typesDict[typ] = [nodeCounter, 1]
            nodeCounter += 1

    questions = {}
    for i in range(n):
        question = lines[counter].split()
        counter += 1
        try:
            questions[(question[1], question[2])] += 1
        except:
            questions[(question[1], question[2])] = 1

    # first connect source to difficulties
    for key in difficultiesDict:
        v, c = difficultiesDict[key]

        G.add_edge(0, v, capacity=c)
    # then connect types to dest
    for key in typesDict:
        v, c = typesDict[key]

        G.add_edge(v, nodeCounter, capacity=c)
    # now fill in middle between difficulties and types
    for key in questions:
        typ, dif = key
        c = questions[key]
        try:
            typV = typesDict[typ][0]
            difV = difficultiesDict[dif][0]

            G.add_edge(difV, typV, capacity=c)
        except:
            pass


    s = 0
    t = nodeCounter
    if networkx.maximum_flow_value(G, s, t) == m:
        print("Yes")
    else:
        print("No")