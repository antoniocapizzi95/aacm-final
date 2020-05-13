import random
import matplotlib.pyplot as plt


def createNode(color):
    return {'color': color, 'edges': []}


def addEdge(g, u, v):
    if v not in g[u]['edges'] and u not in g[v]['edges']:
        g[u]['edges'].append(v)
        g[v]['edges'].append(u)


def createSeedNetwork():
    g = {}
    for i in range(8):
        if i < 4:
            g[i] = createNode("blue")
        else:
            g[i] = createNode("red")
    return g


def createOtherNodes(N, r, g): # creating other nodes based on r parameter
    for i in range(8, N): # N - 8 nodes
        x = random.uniform(0, 1)
        if x <= r:
            g[i] = createNode("red")
        else:
            g[i] = createNode("blue")


def createEdges(g, p):
    q = 1 - p  # calculating q probability
    for i in g:
        for j in g:
            if i == j:
                continue
            x = random.uniform(0, 1)  # generating random number
            if x <= p and g[i]['color'] == g[j]['color']:  # checking if random number is within probability value p and if colors of two nodes are equal
                addEdge(g, i, j)
                continue

            if x <= q and g[i]['color'] != g[j]['color']:  # checking if random number is within probability value q and if colors of two nodes are different
                addEdge(g, i, j)


def degree(g, v):
    return len(g[v]['edges'])


def degreeDistribution(g):
    if not g:
        print("Error: Graph is empty")
        return

    degrees = []
    for v in g:
        d = degree(g, v)
        degrees.append(d)

    nodes = len(g)  # number of nodes
    distribution = {}

    for d in range(nodes):
        count = degrees.count(d)  # checking how much times a degree is repeated in degrees list
        distribution[d] = count / nodes  # calculating the distribution

    return distribution

# --------------------------------------------------------------------------------------------------
g = createSeedNetwork()
N = int(input("Insert the value of N "))
r = float(input("Insert the value of r "))
p = float(input("Insert the value of p "))
createOtherNodes(N, r, g)
createEdges(g, p)
d = degreeDistribution(g)
print(d)

# preparing data to be represented on a plot
lists = sorted(d.items())  # sorted by key, return a list of tuples

x, y = zip(*lists)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set(xlabel='Degree', ylabel='Nodes %',
       title='Degree distribution with ' + str(N) + " nodes, p= " + str(p) + " r=" + str(r))
ax.grid()

# fig.savefig("plot r fixed "+str(r)+" and p "+str(p)+".png")
# fig.savefig("plot p fixed " + str(p) + " and r " + str(r) + ".png")
plt.show()
