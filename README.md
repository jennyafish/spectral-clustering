Spectral Clustering
===================

Dividing data into clusters is a current topic of interest for computer and data scientists. While there are different methods of clustering data points, certain algorithms are more useful for identifying different trends or patterns in a data set.

Algorithm
---------
1. Build a weighted similarity graph such that two data points are connected by an edge with a higher weight if they are more similar, or a lower weight if they are more dissimilar. We used the Gaussian kernel similarity function.
2. Build the normalized Laplacian matrix for the graph.
3. Create a matrix using the eigenvectors corresponding to the k largest eigenvalues of the above Laplacian matrix as columns. Each row of this matrix now corresponds to a data point, but with reduced dimensionality.
4. Use a k-means clustering algorithm to cluster these points.

Links
-----
[Original Assignment](http://math.cmu.edu/~mradclif/teaching/241F18/FinalProjectDescription.pdf)
https://www.cs.cmu.edu/~aarti/Class/10701/slides/Lecture21_2.pdf
https://www.cs.cmu.edu/~aarti/Class/10701/readings/Luxburg06_TR.pdf

https://en.wikipedia.org/wiki/K-means_clustering#Standard_algorithm
https://en.wikipedia.org/wiki/Laplacian_matrix#Symmetric_normalized_Laplacian_2
https://en.wikipedia.org/wiki/Degree_matrix

https://csustan.csustan.edu/~tom/clustering/GraphLaplacian-tutorial.pdf

Pyplot stuff for later :D
https://medium.com/activewizards-machine-learning-company/top-15-python-libraries-for-data-science-in-in-2017-ab61b4f9b4a7
https://matplotlib.org/mpl_toolkits/mplot3d/tutorial.html
