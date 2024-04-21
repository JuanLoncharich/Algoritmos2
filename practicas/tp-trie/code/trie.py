import dictionary as dict
class Trie:
    root = None

class TrieNode:
    parent = None
    children = None
    key = None
    isEndOfWord = False

def printTrie(node, level=0):
    if node is None:
        return
    print('    ' * level, end='')
    if node.key is not None:
        print(node.key)
    for child in node.children:
        printTrie(child, level + 1)


##Insert a word in the trie(using hash tables)
# m is the number of elements we want for each hash table

def insertHash(t,word,m):
    if t.root is None:
        t.root = TrieNode()
        t.root.children = [None] * m
    current = t.root
    
    for char in word:
        found = False
        
        if dict.search(current.children,char) is not None:
            found = True
            current = current.children[dict.hashFunction(char,m)]
            for i in range(0,len(current)):
                if current[i][0] == char:
                    current = current[i][1]
                    break
                    
        if found is False:
            new_node = TrieNode()
            new_node.key = char
            new_node.children = [None] * m
            new_node.parent = current
            current.children = dict.insert(current.children,char,new_node)
            current = new_node
    current.isEndOfWord = True

##Search a word in the trie(using hash tables)

def searchHash(t,word):
    current = t.root
    for char in word:
        nextNode = dict.search(current.children,char)
        if nextNode is not None:
            current = nextNode
            if current.isEndOfWord is True and char == word[-1]:
                return True
        else:
            break
    return False

##Insert a word in the trie(created using python dictionaries)

def insertTrieDict(t,word):
    if t.root is None:
        t.root = TrieNode()
        t.root.children = {}
    current = t.root
    for char in word:
        found = False
        if char in current.children:
            found = True
            current = current.children[char]
        if found is False:
            newNode = TrieNode()
            newNode.key = char
            newNode.children = {}
            newNode.parent = current
            current.children[char] = newNode
            current = newNode
    current.isEndOfWord = True

##Insert a word in the trie(using python lists)

def insert(t,word):
    if t.root is None:
        t.root = TrieNode()
        t.root.children = []
    current = t.root
    for i in range(len(word)):
        found = False
        for child in current.children:
            if child.key == word[i]:
                current = child
                found = True
                break
        if found is False:
            new_node = TrieNode()
            new_node.key = word[i]
            new_node.children = []
            new_node.parent = current
            current.children.append(new_node)
            current = new_node
            if i == len(word) - 1:
                current.isEndOfWord = True

##Search a word in the trie(using python lists)

def search(t,word):
    if t.root is None:
        return False
    current = t.root
    for i in range(0,len(word)):
        for char in current.children:
            if char.key == word[i]:
                current = char
                if i == len(word)-1 and current.isEndOfWord is True:
                    return True
                break
    return False

##Delete a word in the trie(using python lists)

def delete(t,word):
    if t.root is None:
        return False
    deleteR(t.root,word,0)
    
def deleteR(node,word,index):
    if index == len(word):
        if node.isEndOfWord is False:
            return False
        node.isEndOfWord = False
        return len(node.children) == 0
    char = word[index]
    child = None
    for i in range(0,len(node.children)):
        if node.children[i].key == char:
            child = node.children[i]
            break
    if child is None:
        return False
    deleteNode = deleteR(child,word,index+1)
    if deleteNode is True:
        node.children.remove(child)
        return len(node.children) == 0
    return False

##Exercise 4
def prefixLongN(t,prefix,n):
    if t.root is None:
        return []
    lst = []
    current = searchReturnNode(t,prefix)
    return prefixLongNR(current,prefix,n,lst)

def prefixLongNR(node,prefix,n,lst):
    if node is None:
        return None
    if len(prefix) > n:
        return None
    if node.isEndOfWord is True and len(prefix) == n:
        print(prefix)
        return
    for child in node.children:
        prefixLongNR(child,prefix+child.key,n,lst)
        
def searchReturnNode(t,word):
    if t.root is None:
        return False
    current = t.root
    for i in range(0,len(word)):
        for char in current.children:
            if char.key == word[i]:
                current = char
                if i == len(word)-1:
                    return current
                break
    return False

##Exercise 5
def isEqual(t1,t2):
    if t1.root is None and t2.root is None:
        return True
    if t1.root is None or t2.root is None:
        return False
    return isEqualR(t1.root,t2.root)

def isEqualR(node1,node2):
    if node1.isEndOfWord != node2.isEndOfWord:
        return False
    if len(node1.children) != len(node2.children):
        return False
    for i in range(0,len(node1.children)):
        if node1.children[i].key != node2.children[i].key:
            return False
        if isEqualR(node1.children[i],node2.children[i]) is False:
            return False
    return True
    
t = Trie()
insert(t,"hola")
insert(t,"holanda")
insert(t,"holande")


