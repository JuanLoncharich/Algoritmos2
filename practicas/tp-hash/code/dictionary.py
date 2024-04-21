import random
import math

def hashFunction(k,m):
    hash_value = 0
    k = str(k)
    if len(k) == 1:
        random.seed(ord(k))
        for i in range(1,ord(k)):
            hash_value = (hash_value + ord(k) * random.randint(2, 1000))
        return hash_value % m
    else:
        for i in range(1,len(k)):
            random.seed(ord(k[i]))
            for j in range(0,ord(k[i])):
                hash_value = (hash_value + ord(k[i]) * random.randint(2, 1000)) % m
        return hash_value

def insert(d,key,value):
    index = hashFunction(key,len(d))
    if d[index] is None:
        d[index] = [(key,value)]
    else:
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



'''
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
