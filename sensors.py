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