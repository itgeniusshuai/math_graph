# coding:utf-8

import matplotlib.pyplot as plt
import numpy as np

# 画正弦
def drawSin(startX, endX):
    X = np.linspace(startX, endX, 256, endpoint=True).astype(float)  # -π to+π的256个值
    S = np.sin(X)
    plt.plot(X, S)

# 画余弦
def drawCos(startX, endX):
    X = np.linspace(startX, endX, 256, endpoint=True).astype(float)  # -π to+π的256个值
    C = np.cos(X)
    plt.plot(X, C)

# 画正切
def drawTan(startX, endX):
    X = np.linspace(startX, endX, 256, endpoint=True).astype(float)  # -π to+π的256个值
    C = np.tan(X)
    plt.plot(X, C)

# 指定函数
def drawByFunc(startX, endX, func):
    X = np.linspace(startX, endX, 256, endpoint=True).astype(float)  # -π to+π的256个值
    C = list(map(lambda x:func(x),X))
    plt.plot(X, C)