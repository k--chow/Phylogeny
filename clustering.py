import editdistance
import scipy.spatial.distance as ssd
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.spatial.distance import pdist
import numpy as np

labels = ['human','chimp','asiatic toad','black titi','saki','lemur','mouse','snub-nosed monkey']
a = [[0L, 1501L, 6399L, 4258L, 4345L, 4747L, 4760L, 3662L], [1501L, 0L, 6359L, 4249L, 4325L, 4724L, 4739L, 3591L], [6399L, 6359L, 0L, 6344L, 6393L, 6279L, 6393L, 6455L], [4258L, 4249L, 6344L, 0L, 3158L, 4606L, 4738L, 4305L], [4345L, 4325L, 6393L, 3158L, 0L, 4652L, 4840L, 4362L], [4747L, 4724L, 6279L, 4606L, 4652L, 0L, 4718L, 4722L], [4760L, 4739L, 6393L, 4738L, 4840L, 4718L, 0L, 4738L], [3662L, 3591L, 6455L, 4305L, 4362L, 4722L, 4738L, 0L]]
#print a
distArray = ssd.squareform(a)
"""
b = [[5, 10], [10, 15], [15, 20]]
c = ['ayy', 'bee', 'cee']
Y = pdist(c, lambda k, e: editdistance.eval(k, e))
X = pdist(b, 'euclidean')

print X
print Y
"""
#z = linkage(b, method='single', metric='Y')
#print z
print distArray
z = linkage(distArray) #euclidean and simple
x = linkage(a)

print z
print x

d = dendrogram(z,labels=labels)
print d
plt.title('Hierarchical Clustering Dendrogram based on mitochondiral DNA(mtDNA)')
plt.ylabel('mtDNA Levenshtein Distance')
plt.xlabel('Species')
plt.show()
