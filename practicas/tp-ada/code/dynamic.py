
def darCambio(cambio,monedas):
    tabla = [float('inf')] * (cambio + 1)
    tabla[0] = 0
    for i in range(1,cambio+1):
        tabla[i] = tabla[i-1] + 1
        for moneda in monedas:
            if i >= moneda:
                newPosValue = i - moneda
                tabla[i] = min(tabla[i],(tabla[newPosValue] + 1))
    return tabla[-1]


def sumaEnteros(a,k):
    a.sort()
    a = [ak for ak in a if ak <= k]
    
    sumas = [False] * (k+1)
    sumas[0] = True
    
    for num in a:
        for j in range(k, num - 1, -1):
            if sumas[j - num]:
                sumas[j] = True
                break
            
    return sumas[k]
    
def camino(tabla):
    n = len(tabla)
    matriz = [[float('inf')] * n for _ in range(n)]
    matriz[0][0] = tabla[0][0]
    for i in range(1,n):
        matriz[i][0] = tabla[i][0] + tabla[i-1][0]
        matriz[0][i] = tabla[0][i] + tabla[0][i-1]
    for i in range(1,n):
        for j in range(1,n):
            matriz[i][j] = min(matriz[i-1][j],matriz[i][j-1]) + tabla[i][j]
    return matriz[-1][-1]
    

#tabla = [[1,2,7],[3,8,6],[1,1,1]]
#print(camino(tabla))

#print(sumaEnteros([7,8],15))
#print(darCambio(20, [1, 3, 11, 7, 12]))
    
    
    
    