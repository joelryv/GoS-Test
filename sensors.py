import numpy as np

class Sensor:
    def __init__(self, task, x, y):
        self.x = x
        self.y = y
        self.nextTask = ''
        if task == '':
            self.task = np.random.choice(['a', 'i'])
        else:
            self.task = task
        self.vecindad = []
        self.tiempoActivo = 0
        self.tiempoInactivo = 0
        self.bateria = 100

    def creaVecindad(self, sensores, txRange):
        for sensor in sensores:
            if self != sensor:
                if (self.x-sensor.x)**2 + (self.y-sensor.y)**2 <= txRange**2: # Vecindad de Moore de radio 1
                    self.vecindad.append(sensor)

    def activos(self):
        self.vecinosActivos = 0
        for elemento in self.vecindad:
            if elemento.task!='i':
                self.vecinosActivos += 1

    def juegoVida(self):
        if self.task == 'a':
            self.nextTask = 'a'
            self.bateria -= 1
            if self.vecinosActivos < ((2/len(self.vecindad))*8):
                self.nextTask = 'i'
            if self.vecinosActivos > ((3/len(self.vecindad))*8):
                self.nextTask = 'i'
        elif self.task == 'i':
            self.nextTask = 'i'
            rb = int((3/len(self.vecindad))*8)
            if self.vecinosActivos == rb:
                self.nextTask = 'a'
    
    def cicloTrabajo(self):
        if self.task == 'a':
            self.tiempoActivo += 1
            self.tiempoInactivo = 0
        if self.task == 'i':
            self.tiempoInactivo += 1
            self.tiempoActivo = 0
        if self.tiempoActivo >= 10:
            self.nextTask = 'i'
        if self.tiempoInactivo >= 10:
            self.nextTask = 'a'