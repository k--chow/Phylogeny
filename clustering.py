import editdistance
import scipy.spatial.distance as ssd
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage, single, complete, average, weighted, centroid, median, ward
from scipy.spatial.distance import pdist
import numpy as np

labels = ['human','chimp','asiatic toad','black titi','saki','lemur','mouse','snub-nosed monkey']
#a = [[0L, 1501L, 6399L, 4258L, 4345L, 4747L, 4760L, 3662L], [1501L, 0L, 6359L, 4249L, 4325L, 4724L, 4739L, 3591L], [6399L, 6359L, 0L, 6344L, 6393L, 6279L, 6393L, 6455L], [4258L, 4249L, 6344L, 0L, 3158L, 4606L, 4738L, 4305L], [4345L, 4325L, 6393L, 3158L, 0L, 4652L, 4840L, 4362L], [4747L, 4724L, 6279L, 4606L, 4652L, 0L, 4718L, 4722L], [4760L, 4739L, 6393L, 4738L, 4840L, 4718L, 0L, 4738L], [3662L, 3591L, 6455L, 4305L, 4362L, 4722L, 4738L, 0L]]
matrix = []
with open('matrix.txt', 'r') as f:
    for line in f:
        line = line.split()
        if line:
            line = [int(i) for i in line]
            matrix.append(line)

print matrix

#print a
distArray = ssd.squareform(matrix)

#z = linkage(b, method='single', metric='Y')
#print z
print distArray
z = linkage(distArray) #euclidean and simple
print z
x = single(distArray)
print x
y = complete(distArray)
print y
a = average(distArray)
print a
b = weighted(distArray)
print b
"""
c = centroid(distArray)
print c
m = median(distArray)
print m
w = ward(distArray)
print w
"""


#d = dendrogram(z,labels=labels)
#d1 = dendrogram(x, labels=labels)
d2 = dendrogram(w, labels=labels)
plt.figure(1)
plt.title('Hierarchical Clustering Dendrogram based on mitochondrial DNA(mtDNA)')
plt.ylabel('mtDNA Levenshtein Distance')
plt.xlabel('Species')
plt.show()
