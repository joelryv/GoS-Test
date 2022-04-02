import numpy as np
from sensors import Sensor
import matplotlib.pyplot as plt

def creaNodos(n, areaX, areaY):
    nodos = []
    for _ in range(n):
        x = np.random.random()*areaX
        y = np.random.random()*areaY
        nodos.append(Sensor('', x, y))
    return nodos

def creaVecindades(nodos, txRange):
    for nodo in nodos:
        nodo.creaVecindad(nodos, txRange)

def dinamica(nodos):
    for nodo in nodos:
        if nodo.bateria <= 0:
            for vecino in nodo.vecindad:
                vecino.vecindad.remove(nodo)
            nodos.remove(nodo)
            break
        nodo.activos()
        nodo.juegoVida()
        nodo.cicloTrabajo()
    for nodo in nodos:
        nodo.task = nodo.nextTask

def getCoverage(nodos):
    coverage = 0
    for nodo in nodos:
        if nodo.task == 'a':
            coverage += 1
    return coverage

if __name__=='__main__':
    np.random.seed(1)
    allCoverage = []
    for i in range(100):
        coverage = []
        sensores = creaNodos(900, 30, 30)
        creaVecindades(sensores, 2)
        while len(coverage) <= 800:
            coverage.append(getCoverage(sensores)/900)
            dinamica(sensores)
        allCoverage.append(coverage)
    
    maxLen = 0
    for muestra in allCoverage:
        if len(muestra) > maxLen:
            maxLen = len(muestra)
    
    for muestra in allCoverage:
        while len(muestra) < maxLen:
            muestra.append(0)
    
    avrgCoverage = np.average(allCoverage, axis=0)
    plt.plot(avrgCoverage)
    plt.xlabel('Time-steps')
    plt.ylabel('Average coverage [%]')
    plt.show()