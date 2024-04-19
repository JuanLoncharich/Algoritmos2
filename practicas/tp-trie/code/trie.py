import dictionary as dict
class Trie:
    root = None

class TrieNode:
    parent = None
    children = None
    key = None
    isEndOfWord = False

def print_trie(node, level=0):
    if node is None:
        return
    print('    ' * level, end='')
    if node.key is not None:
        print(node.key)
    for child in node.children:
        print_trie(child, level + 1)

##Insert a word in the trie(created using python lists)

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

##Insert a word in the trie(created using hash tables)

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
            print('Entró')
        #print(current.key)
        #print('')
    #print('SALTO')


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


'''
t = Trie()
insert(t, "hola")
insert(t, "holanda")
insert(t, "estas")

print_trie(t.root)

if search(t, "holanda"):
    print("Encontrado")
else:
    print("No encontrado")
'''
t = Trie()
insertHash(t,"hola",15)
insertHash(t,"holanda",15)


#print_trie(t.root)
