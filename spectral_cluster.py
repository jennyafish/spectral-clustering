import numpy
import scipy
import math
from scipy.linalg import eigh
import matplotlib.pyplot

SIG = 5.0 # controls size of neighborhood


# Gaussian kernel similarity function
def get_similarity(d1, d2, sig=5.0):
	# evaluate the similarity between the two points
	if(len(d1) != len(d2)):
		raise Exception()
	sum = 0
	for i in range(len(d1)):
		sum += (d1[i]-d2[i])**2
	sum /= -2*sig*sig
	return math.e**sum
		

def spectral_clustering(input_data, k):
	# first we will construct a similarity graph such that
	# similarity_graph[i][j] is the weight of the connection between
	# the two data points (higher weights are more similar)
	print("Generating similarity graph...")
	similarity_graph = []
	for i in range(len(input_data)):
		row = []
		for j in range(len(input_data)):
			row.append(get_similarity(input_data[i], input_data[j], SIG))
		similarity_graph.append(row)
	# can optimize this later, since symmetric
	
	# now we build a normalized Laplacian matrix for the graph
	# since this is a complete graph, degree matrix D[i][i] = len(input_data)
	laplacian = []
	n = len(input_data)
	# begin with the identity matrix
	L = [[0.0 for x in range(n)] for y in range(n)]
	for i in range(n):
		L[i][i] = 1.0
	# calculate L = I - D^(-1)W
	for i in range(n):
		for j in range(n):
			L[i][j] -= similarity_graph[i][j]/n
	print(L)
	print("Computing eigenvectors...")
	
	# check for linear dependence?
	L = numpy.array(L)
	print(eigh(L))
	N = eigh(L)[1][-k:]
	print(N.T)
	N = N.T
	# normalize row sums to have norm 1
	for i in range(len(N)):
		norm = 0
		for j in range(k):
			norm += N[i][j]**2
		norm = math.sqrt(norm)
		for j in range(k):
			N[i][j] = N[i][j]/norm
	print(N)
	
	# aaaaand cluster by k-means
	
#print(get_similarity([1,30],[0,24]))
spectral_clustering([[0.0,60.0,125.0],[1.0,73.2,153.2],[0.0,65.0,123.0],[1.0,78.2,142.2]], 2)

