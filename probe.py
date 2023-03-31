import networkx as nx
import matplotlib.pyplot as plt
wfg = []


def reset(wfg):
    for i in wfg:
        for j in range(len(i)):
            if i[j] > 1:
                i[j] = 1

def probe(msg):
    if msg[0] == msg[2] and msg[0] != msg[1]:
        print('Deadlock', msg)
        reset(wfg)
        return
    curr = msg[2]

    for i in range(len(wfg[curr])):
        if wfg[curr][i] == 1:
            print('Message from',curr,'to',i)
            print(msg)
            wfg[curr][i] += 1
            probe([msg[0],curr,i])

print('Enter number of processes')
n = int(input())
for i in range(n):
    a = []
    for j in range(n):
        a.append(0)
    wfg.append(a)

print('enter number of edges')
n = int(input())

g = nx.Graph()
print('Enter edges <source> <destination>')
for i in range(n):
    x = list(map(int, input().split()))
    g.add_edge(x[0], x[1])
    wfg[x[0]-1][x[1]-1] = 1

for i in wfg:
    print(i)

print('Enter process that starts probe')
n = int(input())
nx.draw(g,with_labels=True , arrows=True)
probe([n,n,n])
# plt.show()