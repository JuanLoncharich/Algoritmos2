import mylinkedlist
import myqueue

class LinkedList:
  head=None

class Node:
  value=None
  nextNode=None
  
  
class BinaryTree:
  root = None


class BinaryTreeNode:
  key = None
  value = None
  leftnode = None
  rightnode = None
  parent = None

def print_inorder(node):
  if node is not None:

    print_inorder(node.leftnode)
    print(node.key)
    print_inorder(node.rightnode)


def search(b, element):
  return searchR(b.root, element)

def searchR(node, element):
  if node is not None:

    if node.value == element:
      return node.key

    if searchR(node.leftnode, element) != None:
      return searchR(node.leftnode, element)

    if searchR(node.rightnode, element) != None:
      return searchR(node.rightnode, element)


def insert(b, element, key):
  if b.root is None:
    node = BinaryTreeNode()
    node.key = key
    node.value = element
    b.root = node
    return
  else:
    return insertR(b.root, element, key)

def insertR(node, element, key):
  if node is not None:

    if node.key == key:
      return None

    elif node.key > key:
      if node.leftnode is None:
        newNode = BinaryTreeNode()
        newNode.key = key
        newNode.value = element
        newNode.parent = node
        node.leftnode = newNode
      else:
        insertR(node.leftnode,element,key)

    elif node.key < key:
      if node.rightnode is None:
        newNode = BinaryTreeNode()
        newNode.key = key
        newNode.value = element
        newNode.parent = node
        node.rightnode = newNode
      else:
        insertR(node.rightnode,element,key)
    
  
def delete(b,element):
  return deleteR(b.root,element)

def deleteR(node,element):
  if node is not None:
    if node.value == element:
      
      if node.leftnode is None and node.rightnode is None:
        if node.parent.leftnode == element:
          node.parent.leftnode = None
        else:
          node.parent.rightnode = None
        return None
      
      elif node.leftnode is None:
        a = node.rightnode
        node.rightnode.parent = node.parent
        if node.parent.leftnode.value == element:
          node.parent.leftnode = node.rightnode
        else:
          node.parent.rightnode = node.rightnode
        node = None
        return a
        
      elif node.rightnode is None:
        a = node.leftnode
        node.leftnode.parent = node.parent
        if node.parent.leftnode.value == element:
          node.parent.leftnode = node.leftnode
        else:
          node.parent.rightnode = node.leftnode
        node = None
        return a
      
      else:
        menor_mayor = menor_mayores(node.rightnode)
        if menor_mayor.rightnode is None and menor_mayor.leftnode is None:
          a = True
        else:
          a = False
        node.key = menor_mayor.key
        node.value = menor_mayor.value
        
        if a is True:
          if menor_mayor.parent.leftnode.value == menor_mayor.value:
            menor_mayor.parent.leftnode = None
          else:
            menor_mayor.parent.rightnode = None
        else:
          node.rightnode = deleteR(node.rightnode,menor_mayor.key)

    deleteR(node.leftnode,element)
    deleteR(node.rightnode,element)
    

def deleteKey(b,key):
  return deleteKeyR(b.root,key)

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
  

def access(b, key):
  return accessR(b.root, key)

def accessR(node, key):
  if node is not None:

    if node.key == key:
      return node.value

    if accessR(node.leftnode, key) is not None:
      return accessR(node.leftnode, key)

    if accessR(node.rightnode, key) is not None:
      return accessR(node.rightnode, key)


def update(b, element, key):
  return updateR(b.root, element, key)

def updateR(node, element, key):
  if node is not None:

    if node.key == key:
      node.value = element
      return node.key

    if updateR(node.leftnode, element, key):
      return updateR(node.leftnode, element, key)
    if updateR(node.rightnode, element, key):
      return updateR(node.rightnode, element, key)



def traverseInOrder(b):
  l = LinkedList()
  traverseInOrderR(b.root,l)
  return l

def traverseInOrderR(node,l):
  
  if node is not None:
    traverseInOrderR(node.leftnode,l)
    myqueue.enqueue(l,node.value)
    traverseInOrderR(node.rightnode,l)
    

def traverseInPostOrder(b):
  l = LinkedList()
  traverseInPostOrderR(b.root,l)
  return l

def traverseInPostOrderR(node,l):
  
  if node is not None:
    traverseInPostOrderR(node.leftnode,l)
    traverseInPostOrderR(node.rightnode,l)
    myqueue.enqueue(l,node.value)    
    

def traverseInPreOrder(b):
  l = LinkedList()
  traverseInPreOrderR(b.root,l)
  return l

def traverseInPreOrderR(node,l):
  
  if node is not None:
    traverseInPreOrderR(node.leftnode,l)
    traverseInPreOrderR(node.rightnode,l)
    myqueue.enqueue(l,node.value)   
    

def traverseBreadFirst(b):
  l = LinkedList()
  q = LinkedList()
  return traverseBreadFirstR(b.root,l,q)

def traverseBreadFirstR(node,l,q):
  
  if node is None:
    return None
  
  currentNode = node
  myqueue.enqueue(l,currentNode)
  
  while mylinkedlist.length(l) > 0:
    
    currentNode = myqueue.dequeue(l)
    
    myqueue.enqueue(q,currentNode.key)
    
    if currentNode.leftnode is not None:
      myqueue.enqueue(l,currentNode.leftnode)

    if currentNode.rightnode is not None:
      myqueue.enqueue(l,currentNode.rightnode)
      
  return q


def print_linked(l):
    currentNode = l.head
    for i in range(0,mylinkedlist.length(l)-1):
        print(currentNode.value)
        currentNode = currentNode.nextNode
    return
  
    


#b = BinaryTree()
#n2 = BinaryTreeNode()
#n1 = BinaryTreeNode()
#n4 = BinaryTreeNode()
#n9 = BinaryTreeNode()
#n6 = BinaryTreeNode()
#n3 = BinaryTreeNode()
#n8 = BinaryTreeNode()
#n7 = BinaryTreeNode()
#n5 = BinaryTreeNode()

#n1.rightnode = n2
#n3.rightnode = n4
#n3.leftnode = n1
#n5.rightnode = n7
#n5.leftnode = n3
#n7.rightnode = n8
#n7.leftnode = n6
#n8.rightnode = n9

#b.root = n5

#n2.parent = n1
#n1.parent = n3
#n4.parent = n3
#n3.parent = n5
#n9.parent = n8
#n6.parent = n7
#n7.parent = n5
#n8.parent = n7

#n1.key = 1
#n2.key = 2
#n3.key = 3
#n4.key = 4
#n5.key = 5
#n7.key = 7
#n8.key = 8
#n9.key = 9
#n6.key = 6

#n6.value = 123
#n6.value = 678

#print(search(b,123))

#insert(b,456,14)

#node = menor_mayores(n3)
#print(node.key)

#delete(b,678)
#deleteKey(b,4)
#binarytreeDeleteChatGPT.deleteKey(b,7)

#print_inorder(b.root)

#print(access(b,6))

#print(access(b,6))
#print(update(b,456,6))
#print(access(b,6))

#print(menor_mayores(b.root.rightnode).key)



#linked = traverseBreadFirst(b)
#print_linked(linked)