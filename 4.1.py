from scipy import linalg
from sympy import solve, Eq, symbols, Matrix
import numpy

m, q, l, k =symbols('m q l k')
M = numpy.array([[k]*9]*9)
M=M-M
M[0][3]=-1/q
M[1][4]=-1/q
M[2][5]=-1/q
M[3][0]=-l-2*m
M[6][0]=-m
M[8][0]=-m
E=numpy.eye(9)
L=M-k*E
L=Matrix(L)
d=Eq(L.det())
print(solve(d, k))
