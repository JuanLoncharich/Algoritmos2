
    
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
        for vertexIns in g[vertex]:
            if vertexIns != 0:
                verifier = True
                break
        if verifier is False:
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

def convertToBfsTree(g,v):
    a = 0


g = createGraph(['A','B','C'],[('A', 'B'), ('A', 'C'), ('B', 'C')])
print(convertToBfsTree(g,'A'))
