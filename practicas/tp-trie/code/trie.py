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

def insert(t, word):
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
        if not found:
            new_node = TrieNode()
            new_node.key = word[i]
            new_node.children = []
            new_node.parent = current
            current.children.append(new_node)
            current = new_node
            if i == len(word) - 1:
                current.isEndOfWord = True

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
        
    

t = Trie()
insert(t, "hola")
insert(t, "holanda")
insert(t, "estas")

print_trie(t.root)

if search(t, "holanda"):
    print("Encontrado")
else:
    print("No encontrado")
