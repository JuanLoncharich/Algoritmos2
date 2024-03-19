import mylinkedlist
import myqueue
import binarytree
import math
import mystack

def searchNode(l,element):
    
    currentNode = l.head
    while currentNode is not None:
        if currentNode.value == element:
            return currentNode
        currentNode = currentNode.nextNode
    return None


def print_linked(l):
    currentNode = l.head
    for i in range(0,mylinkedlist.length(l)-1):
        print(currentNode.value)
        currentNode = currentNode.nextNode
    return
    

def quickSort(l):
    finalList = mylinkedlist.LinkedList()
    quickSortR(l,finalList)
    return finalList


def quickSortR(l,finalList):
    if l.head is None:
        return
    
    if myqueue.length(l) <= 1:
        mylinkedlist.add(finalList,l.head.value)
        return
    
    menor = mylinkedlist.LinkedList()
    mayor = mylinkedlist.LinkedList()

    pivote = mylinkedlist.access(l,myqueue.length(l)-1)
    
    for i in range(0,myqueue.length(l)):
        if mylinkedlist.access(l,i) < pivote:
            mylinkedlist.add(menor,mylinkedlist.access(l,i))
        else:
            mylinkedlist.add(mayor,mylinkedlist.access(l,i))
    
    quickSortR(menor,finalList)
    quickSortR(mayor,finalList)


def mergeSort(l):
    if l.head is None:
        return None
    if myqueue.length(l) <= 1:
        return
    
    list1 = mylinkedlist.LinkedList()
    list2 = mylinkedlist.LinkedList()

    currentNode = l.head
    for i in range(0,math.trunc(myqueue.length(l)/2)):
        mylinkedlist.add(list1,currentNode.value)
        currentNode = currentNode.nextNode
    for j in range(i,myqueue.length(l)-1):
        mylinkedlist.add(list2,currentNode.value)
        currentNode = currentNode.nextNode
    
    
    orden1 = mergeSort(list1)
    orden2 = mergeSort(list2)
    
    
    l.head = None    
    currentNode1 = list1.head
    currentNode2 = list2.head
    
    i = 0
    while currentNode1 is not None and currentNode2 is not None:
        if currentNode1.value < currentNode2.value:
            mylinkedlist.insert(l,currentNode1.value,i)
            currentNode1=currentNode1.nextNode
        else:
            mylinkedlist.insert(l,currentNode2.value,i)
            currentNode2=currentNode2.nextNode
        i = i + 1  
    while currentNode1 is not None:
        mylinkedlist.insert(l,currentNode1.value,i)
        currentNode1=currentNode1.nextNode
    while currentNode2 is not None:
        mylinkedlist.insert(l,currentNode2.value,i)
        currentNode2=currentNode2.nextNode
    


l = mylinkedlist.LinkedList() 

mylinkedlist.add(l,45)
mylinkedlist.add(l,99)
mylinkedlist.add(l,1)
mylinkedlist.add(l,23)
mylinkedlist.add(l,13)
mylinkedlist.add(l,78)
mylinkedlist.add(l,34)
mylinkedlist.add(l,62)

#l = quickSort(l)
mergeSort(l)
print_linked(l)
