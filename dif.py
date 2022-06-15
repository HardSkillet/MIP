import numpy as np
import matplotlib.pyplot as plt


m = float(input())
p = float(input())
k = float(input())

def f1(y1, y):
    return -p/m * y1 - k/m*y
def f2(y, dy1):
    return -(m/p)*dy1 - (k/p)*y

answer = np.empty(100000)
variable = np.empty(100000)

h = 0.00001
y1 = 1
y = 1
x = 0
for i in range(100000):
    dy1 = h*f1(y1, y)
    dy = h*f2(y, dy1)
    y += dy
    y1 += dy1
    x += h
    answer[i] = y
    variable[i] = x

plt.plot(variable, answer)
plt.show()
print(y)
print(x)