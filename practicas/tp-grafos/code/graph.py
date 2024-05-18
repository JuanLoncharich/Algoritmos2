
    
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
    
def isConnected(g):
    for vertex in g:
        for vertexIns in g:
            if existPath(g,vertex,vertexIns) is False:
                return False
    return True

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

def isComplete(g):
    if isConnected(g) is False:
        return False
    for vertex in g:
        if len(g[vertex]) < len(g)-1:
            return False
    return True

#Crea arbol abarcador en base a grafo g


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


#def convertToBfsTree(g,v):

#def convertToDfsTree(g,v):

#def bestRoad(g,v1,v2):

#def isBipartite(g):

#def PRIM(g):

#def KRUSKAL(g):

g = createGraph(['A','B','C','D','E','F','G','H'],[('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E'), ('D', 'F'), ('E', 'F'), ('G', 'H')])
print(countConnections(g))
#print(convertToBfsTree(g,'A'))
