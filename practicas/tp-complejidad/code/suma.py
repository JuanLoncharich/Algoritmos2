from linkedlist import *

def subSearchElement(current, element):
  currentNode = current

  while currentNode is not None:
    if currentNode.value == element:
      return (element)
    currentNode = currentNode.nextNode

  return (None)


def contieneSuma(A,n):
    current = A.head
    while current != None:
        buscSum = n - current.value 
        num1 = current.value
        num2 = subSearchElement(current.nextNode,buscSum)
        if num2 is None:
            current = current.nextNode
        else:
           return [num1,num2]
        
        
L=LinkedList()
add(L,1)
add(L,1)
add(L,2)
add(L,3)
add(L,5)

print(contieneSuma(L,5))

