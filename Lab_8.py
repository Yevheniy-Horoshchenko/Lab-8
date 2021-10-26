import numpy as np
import math
mas_x = [1.5,2.0,2.5,3.0,3.5,4.0]
mas_y = [10.517,10.193,9.807,9.387,8.977,8.637]
h = mas_x[1] - mas_x[0]
print(h)
mas = []
for i in range (len(mas_y)):
    mas.append(mas_y[i] - mas_y[i-1])
mas.pop (0)
print(mas)
mas_1 = []
for j in range (len(mas)):
    mas_1.append(mas[j] - mas[j-1])
mas_1.pop (0)
print(mas_1)
mas_2 = []
for g in range (len(mas_1)):
    mas_2.append(mas_1[g] - mas_1[g-1])
mas_2.pop (0)
print(mas_2)
mas_3 = []
for l in range (len(mas_2)):
    mas_3.append(mas_2[l] - mas_2[l-1])
mas_3.pop (0)
print(mas_3)
y1=1/h*(mas[1]-(mas_1[1])/2+(mas_2[1])/3+(mas_3[1])/4)
y2=1/h**2*(mas_1[1]-mas_2[1]+11/12*mas_3[1])
print (y1)
print (y2)






