# -*- coding: utf-8 -*-

def simple_iteration(phi, x, eps=10e-3, maxiter=100):
    for _ in range(maxiter):
        x_new = phi(x)
        if (abs(x_new - x) <= eps):
            return x_new
        x = x_new
    return x
