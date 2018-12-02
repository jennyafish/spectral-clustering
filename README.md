Spectral Clustering
===================

Dividing data into clusters is a current topic of interest for computer and data scientists. While there are different methods of clustering data points, certain algorithms are more useful for identifying different trends or patterns in a data set.

Algorithm
---------
1. Build a weighted similarity graph such that two data points are connected by an edge with a higher weight if they are more similar, or a lower weight if they are more dissimilar. We used the Gaussian kernel similarity function.
2. Build the normalized Laplacian matrix for the graph.
3. Create a matrix using the eigenvectors corresponding to the k largest eigenvalues of the above Laplacian matrix as columns. Each row of this matrix now corresponds to a data point, but with reduced dimensionality.
4. Use a k-means clustering algorithm to cluster these points.
