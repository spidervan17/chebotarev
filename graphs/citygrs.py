try:
    import matplotlib.pyplot as plt
except:
    raise

import networkx as nx

def graphies(City):
    G = nx.Graph()
    with open(City, 'r') as c:
        for line in c:
            if line:
                punkt1, punkt2, w = line.split()
                G.add_edge(punkt1, punkt2, weight = w)
    return G

def show(G, path):
    pos=nx.shell_layout(G)
    nx.draw_networkx_labels(G,pos,font_size=16, font_family = 'monospace')
    nx.draw_networkx_nodes(G,pos,node_size=700)
    nx.draw_networkx_edges(G,pos,edgelist=G.edges(),width=1)
    nx.draw_networkx_edges(G,pos,edgelist=[(path[i], path[i+1]) for i in range(len(path)-1)],width=5)
    plt.axis('off')
    plt.savefig("simple_path.png")
    plt.show()


def DFS(G, start, return_fired = False):
    styck = [start]
    resgraph = nx.Graph()
    G = nx.to_dict_of_dicts(G)
    fired = {start}
    while styck:
        curr = styck.pop()
        for neighbour in G[curr]:
            if neighbour not in fired:
                fired.add(neighbour)
                resgraph.add_edge(curr, neighbour, weight = G[curr][neighbour]['weight'])
                styck.append(neighbour)
    return resgraph if not return_fired else (resgraph, fired)
#return_fired = False (c)Andrey
def BFS(G, start):
    queue = [start]
    resgraph = nx.Graph()
    G = nx.to_dict_of_dicts(G)
    fired = {start}
    while queue:
        curr = queue.pop(0)
        for neighbour in G[curr]:
            if neighbour not in fired:
                fired.add(neighbour)
                resgraph.add_edge(curr, neighbour, weight = G[curr][neighbour]['weight'])
                queue.append(neighbour)
    return resgraph

def checking(G):
    ch = nx.to_dict_of_dicts(G)
    fired  = set()
    result = set()
    for current in ch:
        if current not in fired:
            check, f  = DFS(G, current, return_fired = True)
            fired |= f
            result.add(check)
    return(result)

def dijkstra(G, start):
    s = {vertex: float('+inf') for vertex in G}
    s[start] = 0
    queue = [start]
    while queue:
        current = queue.pop(0)
        for n in G[current]:
            offers = s[current] + float(G[current][n]['weight'])
            if offers < s[n]:
                s[n] = offers
                queue.append(n)
    return s

G = graphies('City.txt')
#show(G, ['Abakan', 'Minusinsk'])

B = BFS(G, 'Abakan')
#show(B, [])

D = DFS(G,'Abakan')
#show(D, [])

C = checking(G)
#print('The graph is{}connected'.format(' not ' if len(C) > 1 else ' '))
#print('Number of components:', len(C))
#for t in C:
 #   nx.draw_shell(t)
#plt.show()

s = dijkstra(G, 'Abakan')
print('The shotest ways', s)