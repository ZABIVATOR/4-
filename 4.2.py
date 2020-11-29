from scipy import linalg
import matplotlib.pyplot as plt
import numpy

with open('data2.dat', 'r') as f:
	data = f.read().splitlines()
n=int(data[0])
A=[] 
b=[]

for i in range(1, n+2):
	data[i] = data[i].split(' ')
	for j in range(len(data[i])):
		data[i][j] = float(data[i][j])
	if i!=n+1:
		A.append(data[i])
b = numpy.array(data[n+1])


fig, ax=plt.subplots()
ax.bar(numpy.arange(n), linalg.solve(A,b))
plt.show()
