#Ejercicio 4

def ordenMedio(array):
    if len(array) < 2:
        return array
    array.sort()
    return ordenMedioR(array)

def ordenMedioR(array):
    finalArray = []
    listMenor = []
    listMayor = []

    long = int(len(array)/2)
    if long % 2 != 0:
        long += 1
    
    pivote = array[long]
    
    for i in range(0,len(array)):
        if array[i] < pivote:
            listMenor.append(array[i])
    for i in range(0,len(array)):
        if array[i] > pivote:
            listMayor.append(array[i])
            
    for i in range(0,int(len(listMenor)/2)):
        finalArray.append(listMenor[i])
    for i in range(0,int(len(listMayor)/2)):
        finalArray.append(listMayor[i])
    finalArray.append(pivote)
    for i in range(int(len(listMenor)/2),len(listMenor)):
        finalArray.append(listMenor[i])
    for i in range(int(len(listMayor)/2),len(listMayor)):
        finalArray.append(listMayor[i])
    return finalArray

array = [1,2,3,4,5,6,7,8,9,10]
    
#print(ordenMedio(array))
    
