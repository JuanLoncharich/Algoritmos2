class LinkedList:
  head = None


class Node:
  value = None
  nextNode = None


#Imprime la lista
def printList(list):
  current = list.head
  if current == None:
    return(None)
  while current != None:
    print("[", current.value, "]", end="")
    current = current.nextNode
  print("")


#===========================================
#Descripción: Agrega un elemento al comienzo de L, siendo L una LinkedList que representa el TAD secuencia.
def add(list, element):
  nodoAdd = Node()
  nodoAdd.value = element
  nodoAdd.nextNode = list.head
  list.head = nodoAdd
  #el orden de complejidad de add es O(1)


#===========================================
# Descripción: Busca un nodo de la lista que representa el TAD secuencia.

def searchElement(list, element):
  posicion = 0
  currentNode = list.head

  while currentNode is not None:
    if currentNode.value == element:
      return (posicion)
    currentNode = currentNode.nextNode

    posicion = posicion + 1
  posicion = None
  return (posicion)


def searchNode(list, node):
  posicion = 0
  currentNode = list.head

  while currentNode is not None:
    if currentNode == node:
      return (posicion)
    currentNode = currentNode.nextNode

    posicion = posicion + 1
  posicion = None
  return (posicion)
  #el orden de complejidad de add es O(n) porque el peor caso es que recorra la lista hasta el final


#===========================================
# Descripción: Inserta un elemento en una posición determinada de la lista que representa el TAD secuencia.
def insert(L, element, position):
  current = L.head
  currentPos = 0

  if position == 0:
    add(L, element)
    return position

  elif position > 0:
    if current == None: return
    newNode = Node()
    newNode.value = element

    while current.nextNode != None:
      if currentPos + 1 != position:
        current = current.nextNode
        currentPos = currentPos + 1
      else:
        newNode.nextNode = current.nextNode
        current.nextNode = newNode
        return position
    current.nextNode = newNode
    return currentPos + 1
  return
  #el orden de complejidad de insert es O(n) porque el peor caso esque se quiera insertar un elemento en la ultima posicion


#===========================================
# Descripción: Elimina un elemento de la lista que representa el TAD
# secuencia.
# Poscondición: Se debe desvincular el Node a eliminar.
def delete(L, element):
  current = L.head
  position = searchElement(L, element)
  if position == None: return
  if position == 0:
    L.head = L.head.nextNode
    return position

  for i in range(0, position - 1):
    current = current.nextNode
  current.nextNode = current.nextNode.nextNode
  return position

def deleteNode(L, nodo):
  current = L.head
  position = searchNode(L, nodo)
  if position == None: return
  if position == 0:
    L.head = L.head.nextNode
    return position

  for i in range(0, position - 1):
    current = current.nextNode
  current.nextNode = current.nextNode.nextNode
  return position
  #el orden de complejidad de delete es O(n) porque el peor caso es que se quiera borrar el ultimo elemento


#============================================
# Descripción: Calcula el número de elementos de la lista que representa
# el TAD secuencia.
def length(list):
  currentNode = list.head
  cont = 0
  while currentNode != None:
    cont = cont + 1
    currentNode = currentNode.nextNode

  return (cont)
  #el orden de complejidad de length es O(n) porque tiene que recorrer toda la lista


#============================================
# Descripción: Permite acceder a un elemento de la lista en una posición
# determinada.
def access(list, position):
  valor = None
  currentNode = list.head
  tamaño = length(list)
  if position != 0 and position <= tamaño:
    for i in range(0, position):
      currentNode = currentNode.nextNode
    valor = currentNode.value

  if position == 0:
    valor = currentNode.value

  return (valor)
  #el orden de coplejidad de acces es de O(n) porque el peor caso es si entra la for y lo haga hasta la ultima posicion


#============================================
# Descripción: Permite cambiar el valor de un elemento de la lista en
# una posición determinada
def update(list, element, position):
  posicion = None
  currentNode = list.head
  tamaño = length(list)
  if position != 0 and position <= tamaño:
    for i in range(0, position):
      currentNode = currentNode.nextNode

    currentNode.value = element
    posicion = position
  return (posicion)
  #el orden de complejidad de update es O(n) porque el peor caso es que se quiera acceder al value del ultimo elemento


#mueve un nodo de una posicion a otra
def move(list, position_org, position_dest):
  if position_dest == position_org:
    return ()
  currentNode = list.head
  for i in range(position_org + 1):
    if i == position_org:
      moveNode = currentNode

    currentNode = currentNode.nextNode

  if position_org == 0:
    list.head = list.head.nextNode
  else:
    currentNode = list.head
    for i in range(position_org):
      if i == (position_org - 1):
        currentNode.nextNode = currentNode.nextNode.nextNode

      currentNode = currentNode.nextNode

  if position_dest == 0:
    moveNode.nextNode = list.head
    list.head = moveNode
  else:
    currentNode = list.head
    for i in range(position_dest):
      if i == (position_dest - 1):
        moveNode.nextNode = currentNode.nextNode
        currentNode.nextNode = moveNode

      currentNode = currentNode.nextNode

#invierte una lista
def inverted(list):  
  current = list.head
  anterior = None
  siguiente = None
  
  while current != None:
    siguiente = current.nextNode
    current.nextNode = anterior
    anterior = current
    current = siguiente
  
  list.head = anterior
  return(list)

#encuentra el nodo anterior a un nodo dado
def previousNode(list, node):
  current = list.head
  while current.nextNode != node:
    current = current.nextNode

  return(current)