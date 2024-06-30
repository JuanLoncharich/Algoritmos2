def printGraph(g):
    for vertex in g:
        print(vertex,":",g[vertex])

#Usando listas de adyacencia
def createGraph(v,e):
    graph = {}
    for ver in v:
        graph[ver] = []
    
    for edge in e:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    return graph

def insertEdge(g,v1,v2):
    g[v1].append(v2)
    g[v2].append(v1)

#Determina si existe un camino desde v1 a v2

def existPath(g,v1,v2):
    visited = {}
    stack = [v1]
    while stack:
        vertex = stack.pop()
        if vertex == v2:
            return True
        if vertex not in visited:
            visited[vertex] = True
            stack.extend([neighbor for neighbor in g[vertex] if neighbor not in visited])
    return False

#Determina si el grafo es conexo

def isConnected(g):
    for vertex in g:
        for vertexIns in g:
            if existPath(g,vertex,vertexIns) is False:
                return False
    return True

#Determina si el grafo es un árbol

def isTree(g):
    if isConnected(g) is False:
        return False
    if existCycle(g):
        return False
    return True
    
def existCycle(g):
    for vertex in g:
        for vertexIns in g[vertex]:
            if existPath(g,vertex,vertexIns):
                return True
    return False

#Determina si el grafo es completo

def isComplete(g):
    if isConnected(g) is False:
        return False
    for vertex in g:
        if len(g[vertex]) < len(g)-1:
            return False
    return True

#Crea arbol abarcador en base a grafo g
def convertTree(g):
    if g is None or not isConnected(g):
        return None
    if not existCycle(g):
        return g
    longestValue = max(g.items(), key=lambda item: len(item[1]))[0]
    vertexs = [longestValue]
    edges = []
    
    for vertex in g[longestValue]:
        if vertex not in vertexs:
            vertexs.append(vertex)
            edges.append((longestValue, vertex))
            
    g1 = createGraph(vertexs, edges)
    
    while len(vertexs) < len(g):
        for newValue in vertexs:
            for vertex in g[newValue]:
                if vertex not in vertexs:
                    vertexs.append(vertex)
                    edges.append((newValue, vertex))
        g1 = createGraph(vertexs, edges)
    
    return g1
        

#Cuenta la cantidad de componentes conexas en un grafo
def countConnections(g):
    if isConnected(g):
        return 1
    
    conj = [next(iter(g.items()))[0]]
    contador = 1
    return countConnectionsR(g,conj,contador)

def countConnectionsR(g,conj,contador):
    if g is None:
        return None
    for vertex in g:
        if existPath(g,vertex,conj[0]):
            conj.append(vertex)
    for vertex in g:
        if vertex in conj:
            None
        else:
            contador += 1
            conj.append(vertex)
            return countConnectionsR(g,conj,contador)
    return contador

#BFS(Breadth-First Search)

def convertToBfsTree(g,v):
    if g is None:
        return None
    if v not in g:
        return
    colors = {}
    colors[v] = 'gray'
    bfsTree = {}
    
    bfsTree = {vertex: [] for vertex in g}
    
    for vertex in g:
        colors[vertex] = 'white'
    queue = [v]
    while len(queue) != 0:
        ver = queue.pop(0)
        for vertex in g[ver]:
            if vertex != ver:
                if colors[vertex] == 'white':
                    bfsTree[ver].append(vertex)
                    bfsTree[vertex].append(ver)
                    colors[vertex] = 'gray'
                    queue.append(vertex)
        colors[ver] = 'black'
    return bfsTree

#DFS(Depth-First Search)

def convertToDfsTree(g,v):
    if g is None:
        return None
    if v not in g:
        return
    colors = {}
    colors[v] = 'gray'
    dfsTree = {vertex: [] for vertex in g}
    for vertex in g:
        colors[vertex] = 'white'
        
    for vertex in g[v]:
        if colors[vertex] == 'white':
            convertToDfsTreeR(g,vertex,colors,dfsTree)
    return dfsTree

def convertToDfsTreeR(g,v,colors,dfsTree):
    colors[v] = 'gray'
    for vertex in g[v]:
        if colors[vertex] == 'white':
            dfsTree[v].append(vertex)
            convertToDfsTreeR(g,vertex,colors,dfsTree)
    colors[v] = 'black'
    
#Camino más corto(no Dijkstra)    

#def bestRoad(g,v1,v2):

#Determina si el grafo es bipartito

#def isBipartite(g):

def insertWGraph(graph, node1, node2, weight):
    if node1 not in graph:
        graph[node1] = {}
    if node2 not in graph:
        graph[node2] = {}
    graph[node1][node2] = weight
    graph[node2][node1] = weight
    return graph

def createWGraph(matrix):
    graph = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != -1:
                graph = insertWGraph(graph, i, j, matrix[i][j])
    return graph

#Implementa el algoritmo de PRIM
##Suponiendo g conexo
def PRIM(g):
    if g is None:
        return None
    
    conj1 = {}
    conj2 = {vertex: [] for vertex in g}
    edges = []

    startVertex = next(iter(g))
    conj1[startVertex] = g[startVertex]
    del conj2[startVertex]
    
    while conj2:
        min_edge = None
        min_weight = float('inf')
        
        for vertex in conj1:
            for neighbor in g[vertex]:
                if neighbor in conj2 and g[vertex][neighbor] < min_weight:
                    min_weight = g[vertex][neighbor]
                    min_edge = (vertex, neighbor)
        
        if min_edge is None:
            break
        
        vertex, minG = min_edge
        conj1[vertex][minG] = g[vertex][minG]
        edges.append((vertex, minG))
        conj1[minG] = g[minG]
        del conj2[minG]
    
    graph = createGraph(conj1, edges)
    return graph
    
#Implementa el algoritmo de Kruskal

def KRUSKAL(g):
    if g is None:
        return None
    v = [vertex for vertex in g]
    gr = createGraph(v,[])
    edges = {}
    for i in range(len(g)):
        for j in range(len(g)):
            if i in g and j in g[i] and i != j:
                if g[i][j] >= 0:
                    edges[(i,j)] = g[i][j]
    sortedKeys = sorted(edges, key=lambda x: edges[x])
    #while True:
    for edge in sortedKeys:
        if not existPath(gr,edge[0],edge[1]):
            insertEdge(gr,edge[0],edge[1])
    return gr
        

def addEdge(grafo, v1, v2, peso):
    if v1 in grafo and v2 in grafo:
        grafo[v1][v2] = peso
    else:
        raise ValueError("Uno o ambos vértices no existen")


def createDWGraph(v, e):
    grafo = {}
    for ver in v:
        grafo[ver] = {}
    
    for edge in e:
        addEdge(grafo, edge[0], edge[1], edge[2])
        addEdge(grafo, edge[1], edge[0], edge[2])
    
    return grafo

def shortestPath(g,v1,v2):
    if g is None:
        return None
    if not existPath(g,v1,v2):
        return None
    labels = {}
    path = []
    labels[v1] = 0
    discovered = [v1]
    for neighbour in g[v1]:
        labels[neighbour] = g[v1][neighbour]
        discovered.append(neighbour)
        discovered.pop(0)
        
    while discovered:
        for vertex in discovered:
            for neighbour in g[vertex]:
                newLabel = labels[vertex] + g[vertex][neighbour]
                if neighbour in labels:
                    if newLabel < labels[neighbour]:
                        labels[neighbour] = newLabel
                else:
                    labels[neighbour] = newLabel
                    discovered.append(neighbour)

            discovered.pop(0)
    return labels
            


#g = createGraph(['A', 'B', 'C','D', 'E'], [('A', 'B'), ('A', 'C'), ('B', 'C'), ('E', 'A'),('D','E'),('C','E')])
#g = createWGraph([[40, 50, 20, -1, -1], [50, 10, 30, -1, -1], [20, 30, 10, -1, 40], [-1, -1, -1, 10, 50], [-1, -1, 40, 50, 10]])

#{'A': {'B': 40, 'C': 10, 'E': 80}, 'B': {'A': 40, 'C': 30}, 'C': {'A': 10, 'B': 30, 'E': 20}, 'D': {'E': 10}, 'E': {'A': 80, 'D': 10, 'C': 20}}
g = createDWGraph(['A', 'B', 'C','D', 'E'], [('A', 'B',40), ('A', 'C',10), ('B', 'C',30), ('E', 'A',80),('D','E',10),('C','E',20)])
print(shortestPath(g,'D','A'))


