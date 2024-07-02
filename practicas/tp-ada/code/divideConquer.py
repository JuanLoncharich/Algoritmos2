
def busquedaBinaria(lista,x):
    if len(lista) == 0:
        return None
    return busquedaBinariaR(lista,x)
    
def busquedaBinariaR(lista,x):
    if len(lista) == 1:
        if lista[0] == x:
            return True
        else:
            return False
    else:
        if len(lista) % 2 == 0:
            mitad = int(len(lista)/2)
        else:
            mitad = int(len(lista)/2)
        found1 = busquedaBinariaR(lista[mitad:],x)
        found2 = busquedaBinariaR(lista[:mitad],x)
        if found1 or found2:
            return True
    

def busquedaKesimo(lista,k):
    lista.sort()
    return busquedaKesimoR(lista,k)

def busquedaKesimoR(lista,k):
    if len(lista) == 1:
        return lista[0]
    
    medio = lista[int(len(lista) / 2)]
    
    menores = [x for x in lista if x < medio]
    iguales = [x for x in lista if x == medio]
    mayores = [x for x in lista if x > medio]
    
    if k <= len(menores):
        return busquedaKesimoR(menores, k)
    elif k <= len(menores) + len(iguales):
        return medio
    else:
        return busquedaKesimoR(mayores, k - len(menores) - len(iguales))
    

#not working properly
def subsecuenciaCreciente(numeros):
    return findLis(numeros, 0, len(numeros) - 1)

def mergeSequences(seq1, seq2):
    i = j = 0
    merged = []
    while i < len(seq1) and j < len(seq2):
        if seq1[i] < seq2[j]:
            merged.append(seq1[i])
            i += 1
        else:
            j += 1
    merged.extend(seq1[i:])
    return merged

def findLis(nums, left, right):
    if left == right:
        return [nums[left]]
    
    mid = (left + right) // 2
    leftLis = findLis(nums, left, mid)
    rightLis = findLis(nums, mid + 1, right)
    
    combinedLis = mergeSequences(leftLis, rightLis)
    
    return combinedLis
    
    
def distancia(st1, st2):
    return distanciaR(st1, st2)

def distanciaR(st1, st2):
    if not st1:
        return len(st2)
    if not st2:
        return len(st1)
    
    if st1[0] == st2[0]:
        return distanciaR(st1[1:], st2[1:])
    
    replace = 1 + distanciaR(st1[1:], st2[1:])
    
    insert = 1 + distanciaR(st1, st2[1:])
    delete = 1 + distanciaR(st1[1:], st2)
    
    return min(replace, insert, delete)

    
#print(distancia('hola','hqft'))
#print(busquedaBinaria([2,7,5,6,9,12],7))
#print(busquedaKesimo([2,7,5,6,9,12],3))
#print(subsecuenciaCreciente([ 5, 1, 2, 3, 100, 20, 17, 8, 19, 21 ]))