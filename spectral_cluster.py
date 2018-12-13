import numpy
import scipy
import math
from scipy.linalg import eigh
import matplotlib.pyplot

SIG = 100 # controls size of neighborhood


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
		
# calculates Euclidean distance for k-means
def euclidean_distance(d1, d2):
	if(len(d1) != len(d2)):
		raise Exception()
	sum = 0
	for i in range(len(d1)):
		sum += (d1[i]-d2[i])**2
	return math.sqrt(sum)
		
# returns a list representing the centroid of the points in input_data
def new_centroid(input_data):
	# avg represents the new centroid itself, the average of all input_data points
	avg = []
	# iterates through each coordinate and appends to the new point
	for i in range(len(input_data[0])):
		coord = 0
		# sum up the ith coordinate of the data pts
		for j in range(len(input_data)):
			coord += input_data[j][i]
		avg.append(coord/len(input_data))
	return avg
	
# performs k_means clustering on the input data, returning the cluster assignments
# for each corresponding data point in input_data
def k_means(input_data, k):
	dim = len(input_data[0]) # num of coordinates for each point
	centroids = [input_data[i] for i in range(k)]
	cluster_assignments = [0 for i in range(len(input_data))]
	# can change below later to use a flag, but not sure if converges
	for iter in range(20): # arbitrary number to reset centroids
		for point in range(len(input_data)):
			dist = [euclidean_distance(input_data[point], centroids[i]) for i in range(len(centroids))]
			# check which centroid has minimized distance
			for c in range(len(dist)):
				if(dist[c] < dist[cluster_assignments[point]]):
					cluster_assignments[point] = c
		for c in range(len(centroids)):
			centroids[c] = new_centroid([input_data[p] for p in range(len(input_data)) if cluster_assignments[p] == c])
	return input_data,cluster_assignments #temporary fix

# performs spectral clustering on the input_data, returning a list of cluster
# assignments to k distinct clusters for the corresponding data points
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
	
	print("Computing eigenvectors...")
	
	# check for linear dependence?
	L = numpy.array(L)
	# computes the first k eigenvectors
	N = eigh(L)[1][-k:]
	N = N.T
	# normalize row sums to have norm 1
	for i in range(len(N)):
		norm = 0
		for j in range(k):
			norm += N[i][j]**2
		norm = math.sqrt(norm)
		for j in range(k):
			N[i][j] = N[i][j]/norm
	
	print("Performing k-means clustering...")
	# aaaaand cluster by k-means
	return k_means(N, k)
	
# performs spectral clustering on the input_data, returning a list of cluster
# assignments to k distinct clusters for the corresponding data points
def spectral_clustering_epsilon(input_data, k, epsilon=1.0):
	# creates a similarity graph using an epsilon neighborhood graph
	print("Generating similarity graph...")
	similarity_graph = []
	for i in range(len(input_data)):
		row = []
		for j in range(len(input_data)):
			e = euclidean_distance(input_data[i], input_data[j])
			#row.append(e if e > epsilon else 0)
			row.append(1 if e > epsilon else 0)
		similarity_graph.append(row)
	
	### ABOVE SHOULD WORK: PLES MODIFY BELOW
	
	# now we build a normalized Laplacian matrix for the graph
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
	
	print("Computing eigenvectors...")
	
	# check for linear dependence?
	L = numpy.array(L)
	# computes the first k eigenvectors
	N = eigh(L)[1][-k:]
	N = N.T
	# normalize row sums to have norm 1
	for i in range(len(N)):
		norm = 0
		for j in range(k):
			norm += N[i][j]**2
		norm = math.sqrt(norm)
		for j in range(k):
			N[i][j] = N[i][j]/norm
	
	print("Performing k-means clustering...")
	# aaaaand cluster by k-means
	return k_means(N, k)
	
#print(get_similarity([1,30],[0,24]))
#print(spectral_clustering([[0.0,60.0,125.0],[1.0,73.2,153.2],[0.0,65.0,123.0],[1.0,78.2,142.2]], 2))

