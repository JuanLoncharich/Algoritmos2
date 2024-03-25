from algo1 import *

class LinkedList:
    head=None

class Node:
    value=None
    nextNode=None

def add(l,element):
    
    newNode = Node()
    newNode.value = element
    newNode.nextNode = l.head
    l.head = newNode
        
    return


def search(l,element):
    
    currentNode = l.head
    i = 0
    while currentNode is not None:
        if currentNode.value == element:
            return i
        i = i + 1
        currentNode = currentNode.nextNode
    return None
        
        
def insert(l,element,position):
    newNode = Node()
    newNode.value = element
    if position > length(l):
        return None
    else:
        if position == 0:
            newNode.nextNode = l.head
            l.head = newNode
        else:
            
            currentNode = l.head
            for i in range(0,position-1):
                currentNode = currentNode.nextNode
            newNode.nextNode = currentNode.nextNode
            currentNode.nextNode = newNode
    return position


def delete(l,element):
    if length(l) == 0:
        return None
    else:
        newNode = Node()
        newNode.value = element
        currentNode = l.head
        pos = 0
        if currentNode.value == newNode.value:
            l.head = l.head.nextNode
            return pos
        else:
            while currentNode is not None:
                if currentNode.nextNode.value == newNode.value:
                    currentNode.nextNode = currentNode.nextNode.nextNode
                    return pos
                pos = pos + 1
                currentNode = currentNode.nextNode
            return None        
        

def length(l):
    currentNode = l.head
    i = 1
    if currentNode == None:
        return 0
    while currentNode != None:
        currentNode = currentNode.nextNode
        i = i + 1
    return i


def access(l,position):
    if position >= length(l):
        return None
    else:
        currentNode = l.head
        for i in range(0,position):
            currentNode = currentNode.nextNode
        return currentNode.value


def update(l,element,position):
    newNode = Node()
    newNode.value = element
    if position >= length(l):
        return None
    else:
        if position == 0:
            l.head.value = element
        else:
            currentNode = l.head
            for i in range(0,position):
                currentNode = currentNode.nextNode
            currentNode.value = element
        return position
    
