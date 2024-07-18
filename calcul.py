import sympy
import numpy
import matplotlib.pyplot as plt

def row_extract(*vals): # Make function accept infinite
    return list(vals)

def matrix_create(b_type, r1 = None, r2 = None, r3 = None, r4 = None, r5 = None): 
    """ Dynamically creates matrix based on row values (r1-5); b_type signifies whether b is a zero vector (0) or not (1) """
    all_rows = {1: r1, 2: r2, 3: r3, 4: r4, 5: r5} # row arguments put in dictionary, with row number of row as keys
    full_rows = [] # stores rows (in lists) to be put in A
    a_len = 0 # (column) length of A; needed for setting b's length
    for row in all_rows.values(): # iteratively appending rows to full_rows
        if row != None:
            full_rows.append(row)
            a_len += 1

    b = [] # b (constants) in matrix [A b]
    for row in full_rows: # constants in rows iteratively added to b
        b.append([row[-1]])
        del row[-1] # deleting constants from rows before being added to A
    A = numpy.array(full_rows) # A
    z = numpy.zeros([a_len, 1], dtype = int) # zero vectors for tackling Ax = 0

    sol_calculate(A, b, z, b_type) # inserts A, b, z and dtype as arguments to sol_calculate()

def sol_calculate(a, b, z, btype):
    """ Calculates solution(s) of [A c], where c = b if dtype = 1, or c = z if dtype = 0 """
    c = b if btype == 1 else z
    return numpy.linalg.solve(a, c) 