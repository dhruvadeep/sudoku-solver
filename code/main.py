import pycosat
from math import sqrt
# Importing pycoSAT library

# Getting the input file where each line is a test case
def getFile():
    with open('input.txt', 'r') as file:
        return file.readlines()

# Each line is a test case and in every line we have a line or a dot, every location represents a cell
# Create a list with rows and column
def createMatrix(line):
    length_ = sqrt(len(line))
    matrix = []
    for i in range(int(length_)):
        matrix.append(list(line[i*int(length_):i*int(length_)+int(length_)]))
    return matrix


# Testing for matrix and all
# a = getFile()
# for i in a:
#     x = createMatrix(i)
#     for j in x:
#         print(j)
#     print()


# Create a sudoku solver
'''
    Clauses to be maintained
        1. Each cell in puzzle contains at least one value.
        2. Each cell in the puzzle contains at most one value.
        3. Each row in the puzzle should contain all the values.
        4. Each column in the puzzle should contain all the values.
        5. Each smaller block should contain all the values.
        6. The initial setup (values for some of the cells).    
'''

def cell(i, j, k):
    return i*9*9 + j*9 + k + 1
    # Reasoning: 9*9 is the total number of cells, 9 is the number of possible values in each cell
    # The thing is that we are converting 2D to 1D array

def single_cell_check():
    clauses = []
    for i in range(9):
        for j in range(9):
            clause = [cell(i, j, k) for k in range(9)]
            clauses.append(clause)
            for k in range(9):
                for l in range(k+1, 9):
                    clauses.append([-cell(i, j, k), -cell(i, j, l)])
    return clauses

def row_check():
    clauses = []
    for i in range(9):
        for k in range(9):
            for j in range(9):
                clause = [cell(i, j, k) for j in range(9)]
                clauses.append(clause)
                for j in range(9):
                    for l in range(j+1, 9):
                        clauses.append([-cell(i, j, k), -cell(i, l, k)])
    return clauses

def column_check():
    clauses = []
    for j in range(9):
        for k in range(9):
            for i in range(9):
                clause = [cell(i, j, k) for i in range(9)]
                clauses.append(clause)
                for i in range(9):
                    for l in range(i+1, 9):
                        clauses.append([-cell(i, j, k), -cell(l, j, k)])
    return clauses

