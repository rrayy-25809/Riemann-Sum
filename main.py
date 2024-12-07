import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def f(x):
    return x**2

#x = np.arange(0,10)
x = np.linspace(0, 10, 20)
point = np.linspace(0, 10, 100)
plt.figure(figsize=(6,7))

plt.plot(x,f(x))
for i in range(point.size-1):
    position = (point[i],0)
    size = (point[i+1]-point[i], f(point[i+1]))
    shp=patches.Rectangle(position, size[0], size[1], edgecolor = 'deeppink', facecolor = 'lightgray', fill=True,)
    plt.gca().add_patch(shp)
    plt.gca().text(position[0], size[1]/2, f'{round(size[0]*size[1],2)}')
plt.show()