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

#Implementa el algoritmo de PRIM

#def PRIM(g):
    
#Implementa el algoritmo de Kruskal

#def KRUSKAL(g):

g = createGraph(['A', 'B', 'C','D', 'E'], [('A', 'B'), ('A', 'C'), ('B', 'C'), ('E', 'A'),('D','E'),('C','E')])
print(convertToDfsTree(g,'A'))
