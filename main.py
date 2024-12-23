import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def f(x):
    return x**2

x = np.linspace(0, 10, 20)
point = np.linspace(0, 10, 100)
# matplotlib 폰트 설정
plt.rcParams['font.family'] = ['Malgun Gothic', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False
plt.subplots(figsize=(6, 7))
plt.plot(x,f(x))

for i in range(point.size-1):
    position = (point[i],0)
    size = (point[i+1]-point[i], f(point[i+1]))
    rectangle = patches.Rectangle(position, size[0], size[1], edgecolor = 'deeppink', facecolor = 'lightgray', fill=True,)
    plt.gca().add_patch(rectangle)
    plt.gca().text(position[0], size[1]/2, f'{round(size[0]*size[1],2)}')

plt.title('구분구적법')
plt.xlabel('x')
plt.ylabel('f(x)')

plt.show()