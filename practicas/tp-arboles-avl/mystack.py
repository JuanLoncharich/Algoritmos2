from algo1 import *


class LinkedList:
  head = None

class Node:
  value = None
  nextNode = None

def push(s,element):
  
  currentNode = s.head
  
  newNode = Node()
  newNode.value=element
  
  while currentNode.nextNode is not None:
    currentNode=currentNode.nextNode
    
  currentNode.nextNode=newNode

def pop(s):
  if length(s)>0:
    currentNode=s.head
    popeado=""
    while currentNode.nextNode.nextNode is not None:
      currentNode=currentNode.nextNode
    popeado=currentNode.nextNode.value
    currentNode.nextNode=None
    return popeado
  else:
    return None
  
def length(l):
    currentNode = l.head
    i = 0
    if currentNode == None:
        return 0
    while currentNode != None:
        currentNode = currentNode.nextNode
        i = i + 1
    return i
