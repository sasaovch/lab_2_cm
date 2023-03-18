# -*- coding: utf-8 -*-
# import numpy as np

def tangent_method(f, x0, tol=1e-6, maxiter=100):
    x = float(x0)
    fx = f(x)
    for _ in range(maxiter):
        dfx = (f(x + tol) - fx) / tol
        dx = -fx / dfx
        x = x + dx
        fx = f(x)
        if abs(dx) < tol:
            return x
    raise ValueError("Failed to converge after {} iterations".format(maxiter))

def newton_method(f, df, ddf, left_end, right_end, x0, tol=1e-6, maxiter=10):
    if (f(left_end) * f(right_end) >= 0):
        print("Функция должна принимать значения разных знаков на концах отрезков")
        return -1
    if (df(left_end) * df(right_end) <= 0):
        print("Производная меняет знак на отрезке от ", left_end, " до ", right_end)
        return -1
    if (ddf(left_end) * ddf(right_end) <= 0):
        print("Вторая производная меняет знак на отрезке от ", left_end, " до ", right_end)

    x = float(x0)
    for _ in range(maxiter):
        if (df(x) == 0):
            print("Производная равна нулю в точке ", x)
            return -1
        x_new = x - f(x) / df(x)
        print(x_new)
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    raise x_new
