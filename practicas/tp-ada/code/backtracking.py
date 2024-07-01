
def darCambio(cambio,monedas):
    return darCambioR(cambio, monedas, 0, 0, float('inf'))

def darCambioR(cambio, monedas, totalActual, numMonedas, mejor):
    if cambio == 0:
        mejor = min(mejor, numMonedas)
        return mejor
    
    if numMonedas >= mejor:
        return mejor
    for denominacion in monedas:
        if denominacion <= cambio:
            mejor = darCambioR(cambio - denominacion, monedas, totalActual + denominacion, numMonedas + 1, mejor)
    return mejor


def mochila(pesoMax,latas):
    return mochilaR(pesoMax,latas,[],[])
    
def mochilaR(pesoMax, latas, latasActual, mejorLatas):
    if sum(latasActual) > sum(mejorLatas):
        mejorLatas[:] = latasActual[:]
    
    for i, lata in enumerate(latas):
        if sum(latasActual) + lata <= pesoMax:
            latasActual.append(lata)
            mochilaR(pesoMax, latas[i+1:], latasActual, mejorLatas)
            latasActual.pop()
    
    return mejorLatas


def subsecuenciaCreciente(numeros):
    subsecuencia = subsecuenciaCrecienteR(numeros,[0],[0])
    subsecuencia.pop(0)
    return subsecuencia
    
def subsecuenciaCrecienteR(numeros,subsecuencia,mejorSubsecuencia):
    if len(subsecuencia) > len(mejorSubsecuencia):
        mejorSubsecuencia[:] = subsecuencia[:]
    
    for i in range(len(numeros)):
        if numeros[i] > subsecuencia[-1]:
            subsecuencia.append(numeros[i])
            subsecuenciaCrecienteR(numeros[i+1:],subsecuencia,mejorSubsecuencia)
            subsecuencia.pop()
    return mejorSubsecuencia
    

def subconjuntoSuma(numeros, valor):
    return subconjuntoSumaR(numeros, valor, 0)

def subconjuntoSumaR(numeros, valor, sumaActual):
    if sumaActual == valor:
        return True
    if sumaActual > valor or len(numeros) == 0:
        return False
    
    if subconjuntoSumaR(numeros[1:], valor, sumaActual + numeros[0]):
        return True
    
    if subconjuntoSumaR(numeros[1:], valor, sumaActual):
        return True
    
    return False
            
        
    
#print(subconjuntoSuma([8, 6, 7, 5, 3, 10, 9],15))
#print(subsecuenciaCreciente([ 5, 1, 2, 3, 100, 20, 17, 8, 19, 21 ]))
#print(mochila(10,[3,6,8]))
#print(darCambio(14,[1,2,6,8,10]))
