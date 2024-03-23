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

def rotateRight(tree,node):
  if node.parent is not None:
      node.leftnode.parent = node.parent
      node.parent.leftnode = node.leftnode
      node.parent = node.leftnode
  else:
      tree.root = node.leftnode
  if node.leftnode.rightnode is None:
      node.leftnode.rightnode = node
      node.leftnode = None
  else:
      nodeAux = node.leftnode.rightnode
      node.leftnode.rightnode = node
      node.leftnode.parent = None
      node.leftnode = nodeAux
      nodeAux.parent = node
  return node.parent
            
##Realiza una rotación a la izquierda de un árbol binario
            
def rotateLeft(tree,node):
  if node.parent is not None:
      node.rightnode.parent = node.parent
      node.parent.rightnode = node.rightnode
      node.parent = node.rightnode
  else:
      tree.root = node.rightnode
  if node.rightnode.leftnode is None:
      node.rightnode.leftnode = node
      node.rightnode = None
  else:
      nodeAux = node.rightnode.leftnode
      node.rightnode.leftnode = node
      node.rightnode.parent = None
      node.rightnode = nodeAux
      nodeAux.parent = node
  return node.parent

##Calcula el balance factor de todos los nodos del árbol

def calculateBalance(tree):
    return calculateBalanceR(tree.root)

def calculateBalanceR(node):
    if node is None:
        return
    node.bf = altura(node.leftnode) - altura(node.rightnode)
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
         
##Calcular la altura de un arbol

def altura(node):
    if node is None:
      return 0
    else:
      izquierda = altura(node.leftnode)
      derecha = altura(node.rightnode)
      
      if node.leftnode is None and node.rightnode is None:
        return 1

      return max(izquierda,derecha) + 1
  
  
##Insertar nodos dentro de un AVL manteniendo su condicion de AVL

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
        return insertR(node.leftnode,element,key)

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
        return insertR(node.rightnode,element,key)
      
##Complemento de la funcion insert()

def calculateBalanceBranch(node):
  if node is None:
    return None
  
  node.bf = altura(node.leftnode) - altura(node.rightnode)

  if node.bf < -1:
    if node.rightnode.bf > 0:
      rotateRight(tree,node.rightnode)
    rotateLeft(tree,node)
    
  elif node.bf > 1:
    if node.leftnode.bf < 0:
      rotateLeft(tree,node.leftnode)
    rotateRight(tree,node)
    
  return

tree = AVLTree

insert(tree,' ', 10)
insert(tree,' ', 20)
insert(tree,' ', 24)
insert(tree,' ', 26)
insert(tree,' ', 28)
insert(tree,' ', 30)

print_tree(tree)

