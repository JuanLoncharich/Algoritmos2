import math

def hashFunction(k, m):
    hash_value = 0
    k = str(k)
    a = 17921
    for char in k:
        hash_value = (hash_value * a + ord(char)) % m
    return hash_value

def insert(d,key,value):
    index = hashFunction(key,len(d))
    if d[index] is None:
        d[index] = [(key,value)]
    else:
        if key in d[index][0]:
            return None
        d[index].append((key,value))
    return d

def search(d,key):
    index = hashFunction(key,len(d))
    if d[index] is None:
        return None
    else:
        for i in range(0,len(d[index])):
            if d[index][i][0] == key:
                return d[index][i][1]

def delete(d,key):
    index = hashFunction(key,len(d))
    if d[index] is None:
        return None
    else:
        for i in range(0,len(d[index])):
            if d[index][i][0] == key:
                d[index].pop(i)
                return d[index]
    return None

##Ejercicio 3
def hashFunctionMult(k,m):
    return math.floor(m * ((k *(math.sqrt(5)-1)/2) % 1))
#print(hashFunctionMult(65,1000))

##Ejercicio 4
#O(n) where n is the length of the string
def isPermutation(s1,s2):
    if len(s1) != len(s2):
        return False
    d1 = [None] * len(s1)
    d2 = [None] * len(s2)
    
    for char in s1:
        insert(d1,char,char)
    for char in s2:
        insert(d2,char,char)
        
    for i in range(0,len(d1)):
        if d2[hashFunction(s1[i],len(d2))] is None:
            return False
    return True

##Ejercicio 5
#O(n) where n is the length of the list
def checkRepetitions(s):
    d = [None] * len(s)
    for char in s:
        if search(d,char) is None:
            insert(d,char,char)
        else:
            return True
    return False

##Ejercicio 6
def postalCode(d,pc):
    return hashFunction(pc,len(d))

##Ejercicio 7

def countRepetitions(s):
    d1 = [None] * len(s)
    d2 = {}
    for char in s:
        if search(d1,char) is None:
            insert(d1,char,1)
            d2[char] = 1
        else:
            d2[char] += 1
    return str(d2)

##Ejercicio 8
#O(s + p) donde s es la longitud del primer string y p la longitud del segundo
def firstOcurrence(s,p):
    d = [None] * len(s)
    i = 0
    
    for char in s:
        insert(d,char + str(i),i)
        i += 1

    for j in range(0,len(d)):
        if search(d,p[0] + str(j)) is not None:
            aux = j
            break
    if aux is None:
        return None
    
    i = search(d,p[0] + str(aux))
    j = i
    for char in p:
        if search(d,char + str(i)) != i:
            return None
        i += 1
    return j

##Ejercicio 9
#Complejidad promedio de O(n) donde n es la longitud de t
def isIncluded(s,t):
    d = [None] * len(s)
    for char in t:
        insert(d,char,'')
    for char in s:
        if search(d,char) is None:
            return False
    return True


##Ejercicio 10
def hashFunctionOpenAddressing(d,k,m):
    hash_value = 0
    k = str(k)
    a = 17921
    for char in k:
        hash_value = (hash_value * a + ord(char)) % m
    for i in range(0,m):
        if d[hash_value] is not None:
            if hash_value < m:
                hash_value += 1
            else:
                hash_value = 0
        else:
            break
    return hash_value + i

def insertOpenAddressing(d,key,value):
    index = hashFunctionOpenAddressing(d,key,len(d))
    if d[index] is None:
        d[index] = [(key,value)]
    else:
        if key in d[index][0]:
            return None
        d[index].append((key,value))
    return d

def searchOpenAddressing(d,key):
    index = hashFunctionOpenAddressing(d,key,len(d))
    print(index)
    return d[index]



d = [None] * 11
insertOpenAddressing(d,'12',1)
insertOpenAddressing(d,'13',2)
insertOpenAddressing(d,'14',3)
insertOpenAddressing(d,'15',4)
print(searchOpenAddressing(d,'12'))


'''
if isPermutation('hola','hola'):
    print('Son permutaciones')
else:
    print('No son permutaciones')

d = [None] * 11
insert(d,'asdfafsdsaa','1')
insert(d,'holaBuenasTasdaardesComoEstas','2')
insert(d,321112615461,'3')
insert(d,'ju123123li','4')
insert(d,'jq weqrfewan','5')
insert(d,'robe fdsadfrto','6')
insert(d,'312asd fa214','7')
insert(d,'1212asdfa21414512','8')
insert(d,'12312asda sfds d54165','9')
insert(d,'12312dfa21434312','10')
insert(d,'12312af aa sfdf23r23','11')
insert(d,'12312asdfa22','12')
#print(d)
'''

#print(search(d,'12312dfa21434312'))
#delete(d,321112615461)
#print(d)
