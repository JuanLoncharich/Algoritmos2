def existChar(st,c):
    if c in st:
        return True
    return False

def isPalindrome(st):
    if len(st) == 1 or len(st) == 0:
        return True
    for i in range(int(len(st)/2) + 1):
        if st[i] != st[(len(st)-1-i)]:
            return False
    return True

def mostRepeatedChar(st):
    dic = {}
    for char in st:
        if char in dic:
            dic[char] += 1
        else:
            dic[char] = 1
    return max(dic, key=dic.get)

def getBiggestIslandLen(st):
    cont = 1
    mx = 1
    for i in range(1,len(st)-1):
        if st[i] == st[i-1]:
            cont += 1
            if cont > mx:
                mx = cont
        else:
            cont = 1
    return mx

def isAnagram(st1,st2):
    if len(st1) != len(st2):
        return False
    dic1 = {}
    dic2 = {}
    for char in st1:
        if char in dic1:
            dic1[char] += 1
        else:
            dic1[char] = 1
    for char in st2:
        if char in dic2:
            dic2[char] += 1
        else:
            dic2[char] = 1
    for char in st1:
        if dic1[char] != dic2[char]:
            return False
    for char in st2:
        if dic1[char] != dic2[char]:
            return False
    return True

def verifyBalancedParentheses(st):
    stack = []
    for char in st:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return not stack

def reduceLen(st):
    stRes = ''
    i = 0
    while i < len(st) - 1:
        if st[i] != st[i + 1]:
            stRes += st[i]
            i += 1
        else:
            i += 2
    if i < len(st):
        stRes += st[i]
    return stRes

def isContained(st1,st2):
    i = 0
    j = 0
    while i < len(st1):
        if st1[i] == st2[j]:
            j += 1
        if j == len(st2):
            return True
        i += 1
    return False
    
def isPatternContained(string, pattern, c):
    i = 0
    j = 0
    while i < len(string) and j < len(pattern):
        if pattern[j] == c or string[i] == pattern[j]:
            j += 1
        i += 1
    return j == len(pattern)
            

##Implementación de KMP(Knuth-Morris-Prath algorithm)
def KMP(string,pattern):
    i = 0
    j = 0
    table = buildTable(pattern)
    while i < len(string):
        if string[i] == pattern[j]:
            if j == len(pattern) - 1:
                return i - j
            j += 1
            i += 1
        else:
            if j != 0:
                j = table[j-1]
            else:
                i += 1
    return None
            
def buildTable(string):
    table = [0]
    for i in range(1,len(string)):
        table.append(prefixThatSufix(string,i,table[i-1]))
    return table

def prefixThatSufix(string,pos,lastSave):
    if lastSave == 0:
        if string[pos] == string[0]:
            return 1
        else:
            return 0
    if string[pos] == string[lastSave]:
        return lastSave + 1
    return 0

##Implementación de Rabin-Karp
def rabinKarp(string,pattern):
    d = 256
    q = 10
    m = len(pattern)
    n = len(string)
    p = 0
    t = 0
    h = 1
    result = []

    for i in range(m-1):
        h = (h * d) % q

    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(string[i])) % q

    for i in range(n - m + 1):
        if p == t:
            if string[i:i + m] == pattern:
                result.append(i)

        if i < n - m:
            t = (d * (t - ord(string[i]) * h) + ord(string[i + m])) % q

            if t < 0:
                t += q

    return result
    

#[0, 0, 0, 1, 2, 3]
#print(KMP('aaabaabaaabb','baabaa'))
