class AVLTree:
    root = None

class AVLNode:
    parent = None
    leftnode = None
    rightnode = None
    key = None
    value = None
    bf = None

def print_tree(B):
  _print_tree(B.root, 0)

def _print_tree(node, level):
  if node is not None:
    _print_tree(node.rightnode, level + 1)
    print('  ' * level + str(node.key))
    _print_tree(node.leftnode, level + 1)

##Realiza una rotación a la derecha de un árbol binario

def rotateRight(tree, node):
    new_root = node.leftnode
    node.leftnode = new_root.rightnode
    
    if new_root.rightnode is not None:
        new_root.rightnode.parent = node
    
    new_root.parent = node.parent
    
    if node.parent is None:
        tree.root = new_root
    elif node == node.parent.rightnode:
        node.parent.rightnode = new_root
    else:
        node.parent.leftnode = new_root
        
    new_root.rightnode = node
    node.parent = new_root
    
    return new_root
            
##Realiza una rotación a la izquierda de un árbol binario
            
def rotateLeft(tree, node):
    new_root = node.rightnode
    node.rightnode = new_root.leftnode
    
    if new_root.leftnode is not None:
        new_root.leftnode.parent = node
    
    new_root.parent = node.parent
    
    if node.parent is None:
        tree.root = new_root
    elif node == node.parent.leftnode:
        node.parent.leftnode = new_root
    else:
        node.parent.rightnode = new_root
        
    new_root.leftnode = node
    node.parent = new_root
    
    return new_root

##Calcula el balance factor de todos los nodos del árbol

def calculateBalance(tree):
    return calculateBalanceR(tree.root)

def calculateBalanceR(node):
    if node is None:
        return
    node.bf = height(node.leftnode) - height(node.rightnode)
    calculateBalanceR(node.leftnode)
    calculateBalanceR(node.rightnode)

##Rebalancea el árbol de manera que quede balanceado en altura

def reBalance(tree):
  return reBalanceR(tree.root,tree)

def reBalanceR(node,tree):
  if node is None:
    return
  
  if node.bf > 1 or node.bf < -1:
    reBalanceS(node,tree)
    return
  
  reBalanceR(node.leftnode,tree)
  reBalanceR(node.rightnode,tree)

def reBalanceS(node,tree):
  
  if node.bf < -1:
    if node.rightnode.bf > 0:
      rotateRight(tree,node.rightnode)
    rotateLeft(tree,node)
    
  elif node.bf > 1:
    if node.leftnode.bf < 0:
      rotateLeft(tree,node.leftnode)
    rotateRight(tree,node)
         
##Calcular la altura de un arbol en O(log(n))

def height(node):
  if node is None:
    return 0
  return 1 + max(height(node.leftnode), height(node.rightnode))
  
##Insertar nodos dentro de un AVL manteniendo su condicion de AVL en O(log(n))

def insert(b, element, key):
  if b.root is None:
    
    node = AVLNode()
    node.bf = 0
    node.key = key
    node.value = element

    b.root = node
    return
  
  else:
    
    node = insertR(b.root, element, key)
    while node is not None:
      calculateBalanceBranch(node)
      node = node.parent
      
    return

def insertR(node, element, key):
  if node is not None:

    if node.key == key:
      return None

    elif node.key > key:
      if node.leftnode is None:
        newNode = AVLNode()
        newNode.key = key
        newNode.bf = 0
        newNode.value = element
        newNode.parent = node
        node.leftnode = newNode
        return newNode
      else:
        return insertR(node.leftnode, element, key)

    elif node.key < key:
      if node.rightnode is None:
        newNode = AVLNode()
        newNode.key = key
        newNode.bf = 0
        newNode.value = element
        newNode.parent = node
        node.rightnode = newNode
        return newNode
      else:
        return insertR(node.rightnode, element, key)
      
##Complemento de la funcion insert, que calcula el balance factor del nodo enviado y realiza rotaciones correspondientes para balancear el arbol

def calculateBalanceBranch(node):
  if node is None:
    return None
  
  node.bf = height(node.leftnode) - height(node.rightnode)

  if node.bf < -1:
    if node.rightnode.bf > 0:
      rotateRight(tree,node.rightnode)
    rotateLeft(tree,node)
    
  elif node.bf > 1:
    if node.leftnode.bf < 0:
      rotateLeft(tree,node.leftnode)
    rotateRight(tree,node)

  node.bf = height(node.leftnode) - height(node.rightnode)    
  return

##Eliminar nodos dentro de un AVL por su key manteniendo su condicion de AVL en O(n)

def deleteKey(b,key):
  node = deleteKeyR(b.root,key)
  while node is not None:
    calculateBalanceBranch(node)
    node = node.parent
  return

def deleteKeyR(node,key):
  if node is None:
    return node

  if key < node.key:
    node.leftnode = deleteKeyR(node.leftnode, key)
  elif key > node.key:
    node.rightnode = deleteKeyR(node.rightnode, key)
  else:
    if node.leftnode is None:
      a = node.rightnode
      node = None
      return a
    
    elif node.rightnode is None:
      a = node.leftnode
      node = None
      return a

    a = menor_mayores(node.rightnode)
    node.key = a.key
    node.rightnode = deleteKeyR(node.rightnode,a.key)

  return node
    
def menor_mayores(node):
  currentNode = node
  while currentNode.leftnode is not None:
      currentNode = currentNode.leftnode
  return currentNode


tree = AVLTree

insert(tree,' ', 10)
insert(tree,' ', 20)
insert(tree,' ', 24)
insert(tree,' ', 26)
insert(tree,' ', 28)
insert(tree,' ', 30)

deleteKey(tree,20)
deleteKey(tree,24)
deleteKey(tree,10)

print_tree(tree)

