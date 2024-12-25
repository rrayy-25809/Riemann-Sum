import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

def f(x):
    return x**2

x = np.linspace(0, 10, 20)
point = np.linspace(0, 10, 100)
# matplotlib 폰트 설정
plt.rcParams['font.family'] = ['Malgun Gothic', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False
plt.subplots(figsize=(6, 7))
plt.plot(x,f(x))

# 변수 초기화
result = 0

# 구분구적법 적용
for i in range(len(point) - 1):
    position = (point[i], 0)
    size = (point[i + 1] - point[i], f(point[i + 1]))
    rectangle = patches.Rectangle(position, size[0], size[1], edgecolor='deeppink', facecolor='lightgray', fill=True)
    plt.gca().add_patch(rectangle)
    extent = round(size[0] * size[1], 2)
    result += extent
    plt.gca().text(position[0], size[1] / 2, f'{extent}')

# 그래프 제목 및 축 레이블 설정
plt.title('구분구적법')
plt.xlabel('x')
plt.ylabel('f(x)')

# 결과 출력
print(f'적분 결과: {result}')
print(f'적분 결과(실제): {(10**3) / 3}')

# 그래프 표시
plt.show()