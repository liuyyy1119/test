import numpy as np
import matplotlib.pyplot as plt

# 创建一个角度数组
theta = np.linspace(0, 2 * np.pi, 100)

# 使用参数方程表示圆的 x 和 y 坐标
x = np.cos(theta)
y = np.sin(theta)

# 创建图形
plt.figure(figsize=(6, 6))

# 绘制圆
plt.plot(x, y)

# 设置图形的比例，使其为圆形
plt.gca().set_aspect('equal', adjustable='box')

# 设置坐标轴的范围
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)

# 添加标题
plt.title('Circle using numpy and matplotlib')

# 显示图形
plt.show()