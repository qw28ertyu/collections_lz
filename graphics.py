import matplotlib.pyplot as mplt
import numpy as np

#cоздаём диапазон от -5 до 5 
x = np.linspace(-5, 5, 50)
#парабола                  
y = x ** 2
# создание графика
mplt.plot(x, y, color="red",marker='o')

#функция экспоненты (e^x)
y = np.exp(x)
mplt.plot(x, y, color="blue", marker='x') # создание графика

#натуральный логарифм 
log = np.linspace(0.1, 10, 50)
y_log = np.log(log)
mplt.plot(log, y_log, color="pink", marker='s')

y = x**3 #квадратичная парабола
mplt.plot(x, y, color="green", marker='^')
#показ графика                             
mplt.show()     
