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