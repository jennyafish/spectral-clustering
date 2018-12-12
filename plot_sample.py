import numpy
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import spectral_cluster

input_data = [[1.0, 61.6, -1.14], [1.0, 59.3, -1.68], [1.0, 61.7, -0.15], [1.0, 59.8, -1.89], [0.0, 61.5, 2.945], [0.0, 54.4, 0.11], [0.0, 62.2, 3.035], [1.0, 61.8, -0.075], [0.0, 63.6, 3.245], [1.0, 59.9, -2.055], [0.0, 55.1, -0.67], [1.0, 58.2, -2.595], [1.0, 62.0, -1.335], [1.0, 58.4, -2.535], [1.0, 64.4, 4.145], [0.0, 57.0, 0.43], [0.0, 63.9, 3.5], [0.0, 62.8, 4.685], [0.0, 55.9, -0.31], [1.0, 61.9, -2.16], [0.0, 53.6, 0.21], [1.0, 60.8, -2.22], [1.0, 61.3, -1.62], [1.0, 61.9, -1.215], [0.0, 64.4, 2.735], [0.0, 55.1, 0.423], [1.0, 63.0, 3.8], [0.0, 55.6, -0.571], [0.0, 60.6, 2.435], [0.0, 55.6, 0.41], [0.0, 54.4, -0.23], [0.0, 53.2, -0.7], [1.0, 60.8, -2.625], [0.0, 53.3, 0.74], [0.0, 56.3, -0.99], [0.0, 63.5, 2.855], [1.0, 60.5, 5.0], [1.0, 61.7, 2.345], [1.0, 58.3, -1.335], [0.0, 56.1, -0.14], [0.0, 64.0, 2.795], [0.0, 53.4, 0.25], [0.0, 61.2, 2.825], [1.0, 60.7, 3.425], [1.0, 58.6, -2.205], [1.0, 60.9, -1.41], [0.0, 54.3, 0.56], [1.0, 59.3, -1.395], [1.0, 59.7, -0.87], [0.0, 63.2, 4.025]]
x = [input_data[0] for i in range(len(input_data))]
y = [input_data[1] for i in range(len(input_data))]
z = [input_data[2] for i in range(len(input_data))]

# og answer, overwritten immediately
cluster = numpy.array([1, 1, 1, 1, 0, 2, 0, 1, 0, 1, 2, 1, 1, 1, 0, 2, 0, 0, 2, 1, 2, 1, 1, 1, 0, 2, 0, 2, 0, 2, 2, 2, 1, 2, 2, 0, 0, 0, 1, 2, 0, 2, 0, 0, 1, 1, 2, 1, 1, 0])
# answer produced by the algorithm
cluster = spectral_cluster.spectral_clustering(input_data, 3)[1]
# uncomment below to check the modified points
#input_data = spectral_cluster.spectral_clustering(input_data, 3)[0]


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#scatter = ax.scatter(x,y,z, c='r', marker='o')

for k in range(3):
	color = ['r','g','b']
	xs = [input_data[i][0] for i in range(len(input_data)) if cluster[i] == k]
	ys = [input_data[i][1] for i in range(len(input_data)) if cluster[i] == k]
	zs = [input_data[i][2] for i in range(len(input_data)) if cluster[i] == k]
	ax.scatter(xs, ys, zs, c=color[k])

ax.set_xlabel('x')
ax.set_ylabel('y')
#ax.set_zlabel('z')
#plt.colorbar(scatter)

plt.show()