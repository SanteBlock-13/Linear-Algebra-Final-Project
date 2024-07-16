import sympy
import numpy
import matplotlib.pyplot as plt

def row_extract(*vals):# Make function accept infinite
    return list(vals)

def matrix_create(r1 = None, r2 = None, r3 = None, r4 = None, r5 = None):
    all_rows = {1: r1, 2: r2, 3: r3, 4: r4, 5: r5}
    full_rows = []
    a_len = 0
    for row in all_rows.values():
        if row != None: 
            full_rows.append(row)
            a_len = 

    A = numpy.array(full_rows)
    b = []
    for row in full_rows:
        b.append([row[-1]])
    z = numpy.zeros([])