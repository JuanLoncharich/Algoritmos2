from algo1 import *
from mystack import length

class LinkedList:
  head = None

class Node:
  value = None
  nextNode = None

def enqueue(q,element):
  currentNode = q.head
    
  newNode = Node()
  newNode.value=element
  
  if q.head is None:
    q.head = newNode
    
  else:
    while currentNode.nextNode is not None:
      currentNode=currentNode.nextNode
      
    currentNode.nextNode=newNode

def dequeue(q):
  if length(q) > 0:
    dequeuedeado = q.head.value
    q.head = q.head.nextNode
    return dequeuedeado
  else:
    return None

