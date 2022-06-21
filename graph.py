from turtle import color
from matplotlib import pyplot as plt
import numpy as np

resultado = np.loadtxt('resultados.txt')

plt.figure(figsize=(6,3.375))
plt.plot(resultado, color='black', linewidth=2)
plt.xlabel('Time-steps', fontsize=12)
plt.ylabel('Average coverage', fontsize=12)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid()
plt.subplots_adjust(left=0.1, right=0.99, top=0.99, bottom=0.15)
plt.show()