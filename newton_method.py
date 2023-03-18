# -*- coding: utf-8 -*-
import numpy as np
from tabulate import tabulate

def newton_system(F, J, x0, tol=1e-6, maxiter=10):
    """
    Newton's method for solving systems of nonlinear equations

    Parameters:
    F : function
        The system of nonlinear equations as a function of x
    J : function
        The Jacobian of the system of equations as a function of x
    x0 : array-like
        The initial guess for the solution
    tol : float, optional
        The tolerance for convergence
    maxiter : int, optional
        The maximum number of iterations

    Returns:
    x : array-like
        The solution to the system of nonlinear equations
    """

    x = np.asarray(x0)
    for _ in range(maxiter):
        Fx = F(x)
        for i in range(len(Fx)):
            Fx[i] = -Fx[i]
        Jx = J(x)
        matrix = [ [0] * (len(Fx) + 1) for i in range(len(Fx))]
        for i in range(len(Fx)):
            for j in range(len(Fx)):
                matrix[i][j] = Jx[i][j]
            matrix[i][len(Fx)] = Fx[i] 
        # dx = np.asarray(iterate_matrix(matrix, tol, len(Fx)))
        # dx = solve(Jx, Fx)
        # dx = np.linalg.solve(Jx, Fx)
        dx = gauss_method(matrix)
        x = np.add(x, dx)
        if np.linalg.norm(dx) < tol:
            return x
    raise ValueError("Failed to converge after {} iterations".format(maxiter))

def diagonal_matrix(matrix):
    is_valid = True
    for i in range(len(matrix)):
        if matrix[i][i] != 0:
            for j in range(i + 1, len(matrix)):
                ratio = matrix[j][i] / matrix[i][i]
                for k in range(len(matrix)+1):
                    matrix[j][k] = matrix[j][k] - ratio * matrix[i][k]
        else:
            is_valid = False
            break
    if is_valid:
        return matrix
    else:
        return []


def solving_equations(matrix):
    answer = []
    for i in range(len(matrix) - 1, -1, -1):
        k = matrix[i][i]
        right = matrix[i][len(matrix)]
        left = 0
        index = 0
        for j in range(len(matrix) - 1, i, -1):
            left += (matrix[i][j] * answer[index])
            index += 1
        solution = (right - left) / k
        answer.append(solution)
    return answer


def gauss_method(matrix):
    if not is_matrix_valid(matrix):
        return {}
    matrix = diagonal_matrix(matrix)
    if len(matrix) == 0:
        return {}
    answer = solving_equations(matrix)
    answer = answer[::-1]
    return answer

def is_matrix_valid(matrix):
    try:
        rows = len(matrix)
        for i in range(1, rows):
            if len(matrix[i]) != len(matrix[i-1]):
                return False
            if matrix[i][i] == 0:
                return False
        if matrix[0][0] == 0:
            return False
        return True
    except IndexError:
        return False
