import math
import numpy as np  # słowo kluczowe "as" oznacza przesłania nazwę numpy i pozwala
import scipy
import pandas as pd
def cylinder_area(r:float,h:float):
        if r > 0 and h > 0:
        base_area = 2 * math.pi * r ** 2
        wall_area = 2 * math.pi * r * h
        return float(wall_area + base_area)
    else:
        return float('NaN')

def fib(n:int):
    wyrazy = (0, 1)  # dwa pierwsze wyrazy ciągu zapisalem w krotce
    a, b = wyrazy  # przypisanie wielokrotne, rozpakowanie krotki
    vec = np.array([1])
    while n > 1:
        a, b = b, a + b  # przypisanie wielokrotne
        n -= 1
        vec = np.append(vec, b)
    return vec

def matrix_calculations(a:float):
    m = np.array(([[a, 1, -a], [0, 1, 1], [-a, a, 1]]))
    #Inverse of Matrix m
    if np.linalg.det(m) != 0:        #Napisalem warunek na to, aby wyznacznik byl rozny od zera
        m_inv = np.linalg.inv(m)
    else:
        m_inv = float('NaN')           #gdyby wyznacznik byl rowny zero, przypisano by wartosc nan
    # Transpose a Matrix m
    m_t = m.T
    # determinant of the matrix
    m_det = np.linalg.det(m)
    return m_inv, m_t, m_det


def custom_matrix(m:int, n:int):
    data = (m, n)
    if m <= 0 or n <= 0:
        return None
    else:
        a = np.zeros(data)
        for row in range(m):
            for col in range(n):
                if row>col:
                    a[row, col] = row
                else:
                    a[row, col] = col
    return a
