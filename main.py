# -*- coding: utf-8 -*-
from newton_method import newton_system
from simple_iteration_method import simple_iteration
from math import sin, exp, sqrt, cos, asin
from tangent_method import (
    tangent_method,
    newton_method
)

FUNCTIONS = [
    (
    "5 * x^2 - 7 * x - 4 x = -0.4357, x = 1.8357",
    lambda x: 5*x**2 - 7*x - 4
    ),
    (
    "1 / sqrt(x) - 10 x= 0.01",
    lambda x: 1 / sqrt(x) - 10
    ),
    (
    "6 * cos(x)^2 + 5 * sin(x) - 7 x = 0.3398 x = 2.8017",
    lambda x: 6 * (cos(x))**2 + 5 * sin(x) - 7
    ),
    (
    "e^(3x) - 1 x = 0",
    lambda x: exp(3 * x) - 1
    )
]

D_FUNCTIONS = [
    lambda x: 10*x - 7,
    lambda x: -1 / (2 * x * sqrt(x)),
    lambda x: -6 * sin(2*x) + 5 * cos(x),
    lambda x: 3 * exp(3 * x)

]

DD_FUNCTIIONS = [
    lambda x: 10,
    lambda x: 3 / (4 * x**2 * sqrt(x)),
    lambda x: -12 * cos(2*x) - 5 * sin(x),
    lambda x: 9 * exp(3 * x)
]

PHI = [
    lambda x: (5 * x**2 - 4) / 7,
    lambda x: 1 / 100,
    lambda x: asin((7 - 6 * cos(x)**2) / 5),
    lambda x: 0
]

SYSTEM = [
    (
        "0.1 * x^2 + x + 0.2 * y^2 - 0.3 and 12x - 5y ",
        lambda x: [0.1 * x[0]** 2 + x[0] + 0.2 * x[1]**2 - 0.3, 12*x[0] - 5 * x[1]]
    ),
    (
        "sin(x)^2 * cos(y)^2 - 3/16 and -2 * sin(x)**2 + 2 * cos(y)**2 - 1",
        lambda x: [x[0] - sin(2 * x[1]**2 * 2 + 3), -2 * sin(x[0])**2 + 2 * cos(x[1])**2 - 1]
    )
]

Jacoby = [
    lambda x: [[0.2 * x[0] + 1, 0.4 * x[1]], [12, -5]],
    lambda x: [[sin(2*x[0]) * cos(x[1])**2, -sin(x[0]**2)*cos(2*x[1])], [-2*sin(2*x[0]), -2 * sin(2* x[1])]]
]

def main():
    print("Choose your function")
    
    for i, group in enumerate(FUNCTIONS, 1):
        print(i, ": ", group[0], sep="")
    number_of_func = int(input())
    while (number_of_func >= 5 or number_of_func <= 0):
        number_of_func = int(input("Enter number of function: "))
    number = number_of_func - 1
    fun = FUNCTIONS[number][1]
    df = D_FUNCTIONS[number]
    ddf = DD_FUNCTIIONS[number]
    phi = PHI[number]

    approx = float(input("Enter the first approximation: "))
    left_end = float(input("Enter left end for newton method: "))
    right_end = float(input("Enter right end for newton method: "))
    while (right_end <= left_end):
        print("Left end must be smaller than right")
        left_end = float(input("Enter left end for newton method: "))
        right_end = float(input("Enter right end for newton method: "))
    for i, group in enumerate(SYSTEM, 1):
        print(i, ": ", group[0], sep="")
    number_of_sys = int(input())
    while (number_of_sys >= 3 or number_of_sys <= 0):
        number_of_sys = int(input("Enter number of function: "))
    print("Enter first vector")
    vector = map(int, input().split(" "))
    simp_it = simple_iteration(phi, approx)
    print("simple iteration method result:", simp_it)
    newton_m = newton_method(fun, df, ddf, left_end, right_end, approx)
    print("newton_m", newton_m)
    tang = tangent_method(fun, approx)
    print("tang", tang)
    sys_result = newton_system(SYSTEM[number_of_sys - 1][1], Jacoby[number_of_sys - 1], vector)
    print(sys_result)

if __name__ == '__main__':
    main()
