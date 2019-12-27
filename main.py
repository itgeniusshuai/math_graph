# coding:utf-8

import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist
import numpy as np
import line

# fig, ax = plt.subplots()
# y1 = []
# for i in range(50):
#     y1.append(i)  # 每迭代一次，将i放入y1中画出来
#     ax.cla()   # 清除键
#     ax.bar(y1, label='test', height=y1, width=0.3)
#     ax.legend()
#     plt.pause(0.1)
def func(x):
    return x*x/5-1;

if __name__ == "__main__":
    # 创建画布
    fig = plt.figure(figsize=(8, 8))
    # 使用axisartist.Subplot方法创建一个绘图区对象ax
    ax = axisartist.Subplot(fig, 111)
    # 将绘图区对象添加到画布中
    fig.add_axes(ax)

    ax.axis["x"] = ax.new_floating_axis(0, 0)
    ax.axis["x"].set_axisline_style("->", size=1.0)
    #
    ax.axis["y"] = ax.new_floating_axis(1, 0)
    ax.axis["y"].set_axisline_style("-|>", size=1.0)

    plt.xlim(-np.pi,np.pi)
    plt.ylim(-1, 1)
    # line.drawSin(-np.pi,np.pi)
    # line.drawCos(-np.pi,np.pi)
    # line.drawTan(-np.pi/3,np.pi/3)
    line.drawByFunc(-np.pi,np.pi, func)
    plt.show()
