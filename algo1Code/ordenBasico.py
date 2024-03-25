import mylinkedlist
import myqueue


def bubbleSort(l):
    for i in range(0,myqueue.length(l)):
        currentNode = l.head
        for j in range(0,myqueue.length(l)-1):
            if currentNode.value > currentNode.nextNode.value:
                a = currentNode.value
                currentNode.value = currentNode.nextNode.value
                currentNode.nextNode.value = a
            currentNode = currentNode.nextNode
            

def selectionSort(l):
    for i in range(0,myqueue.length(l)):
        menor = mylinkedlist.access(l,i)
        menorPos = i
        for j in range(i,myqueue.length(l)):
            if mylinkedlist.access(l,j) < menor:
                menor = mylinkedlist.access(l,j)
                menorPos = j
        move(l,menorPos,i)
        

def insertionSort(l):
    for i in range(1,myqueue.length(l)):
        act = mylinkedlist.access(l,i)
        for j in range(0,i):
            if act < mylinkedlist.access(l,j):
                mylinkedlist.delete(l,act)
                mylinkedlist.insert(l,act,j)
                break


def move(l,posIn,posFin):
    valueIn = mylinkedlist.access(l,posIn)
    valueFin = mylinkedlist.access(l,posFin)
    
    mylinkedlist.delete(l,valueIn)
    mylinkedlist.insert(l,valueFin,posIn)
    
    mylinkedlist.delete(l,valueFin)
    mylinkedlist.insert(l,valueIn,posFin)
    
    return


def print_linked(l):
    currentNode = l.head
    for i in range(0,mylinkedlist.length(l)-1):
        print(currentNode.value)
        currentNode = currentNode.nextNode
    return


l = mylinkedlist.LinkedList()

mylinkedlist.add(l,1)
mylinkedlist.add(l,13)
mylinkedlist.add(l,23)
mylinkedlist.add(l,34)
mylinkedlist.add(l,45)
mylinkedlist.add(l,62)
mylinkedlist.add(l,78)
mylinkedlist.add(l,99)

#bubbleSort(l)
#selectionSort(l)
insertionSort(l)

print_linked(l)