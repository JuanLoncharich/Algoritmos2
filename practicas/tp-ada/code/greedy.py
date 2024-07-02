
def adminActividades(tareas, inicio, fin):    
    keysDic = sorted(tareas, key=lambda x: x[1])
    
    actividades = [keysDic[0]]
    ultimaActividad = keysDic[0]

    for tarea in keysDic[1:]:
        if tarea[0] >= ultimaActividad[1]:
            actividades.append(tarea)
            ultimaActividad = tarea
    
    return actividades
    
    
def buscaPares(vector):
    sumas = []
    for i in range(int(len(vector)/2)):
        sumas.append(vector[2*i]+vector[2*i+1])
    return max(sumas)


def mochila(pesoMax,latas):
    res = []
    latas.sort(reverse = True)
    for lata in latas:
        if lata < pesoMax:
            res.append(lata)
            pesoMax -= lata
        if pesoMax == 0:
            return res
    return res
    

#print(mochila(10,[3,6,11]))
#print(buscaPares([5,8,1,4,7,9]))    
#print(adminActividades([(1, 4), (3, 5), (0, 3), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)], 1, 12))