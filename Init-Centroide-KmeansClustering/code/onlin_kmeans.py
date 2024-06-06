#!/usr/bin/env python
#### fichier onlin_kmeans.py
"""
class sklearn.cluster.KMeans(
n_clusters=8,
*,
init='k-means++',
n_init=10,
max_iter=300,
tol=0.0001,
precompute_distances='deprecated',
verbose=0,
random_state=None,
copy_x=True,
n_jobs='deprecated',
algorithm='auto')
module initialize_centroids (random,plus_plus,naive_sharding)= fonction (
ds: tableau numpy, ensemble de données à utiliser pour l'initialisation du
centre de gravité.
k: int, le nombre souhaité de clusters pour lesquels des centres de gravité
sont requis.
centroids: numpy array Collection de k centroïds sous forme de tableau
numpy.
)
module onlin_kmeans (random,
kmeansplus_plus,initialize_centroids,online_kmeans,fully_online,)= fonction (
ds: tableau numpy, ensemble de données à utiliser pour l'initialisation du
centre de gravité.
k: int, le nombre souhaité de clusters pour lesquels des centres de gravité
sont requis.
centroids: numpy array Collection de k centroids sous forme de tableau
numpy.
X: matrice de données
C: centres initiaux
eta: 1/n_k diminue progressivement le taux d'apprentissage
f: coût de l'installation
k_target: le nombre de clusters que nous voudrions que l'algorithme produise
)
"""
from math import sqrt, floor
import numpy as np
X = np.vstack(((np.random.randn(150, 2) * 0.75 + np.array([1, 0])),
(np.random.randn(50, 2) * 0.25 + np.array([-0.5, 0.5])),
(np.random.randn(50, 2) * 0.5 + np.array([-0.5, -0.5]))))
def random(C, k, random_state=13):
"""
Créez des centres de gravité de cluster aléatoires.
Paramètres
----------
ds: tableau numpy
Jeu de données à utiliser pour l'initialisation du centre de gravité.
X: matrice de données
k: int
Nombre souhaité de clusters pour lesquels des centres de gravité sont
requis.
Retour
-------
centroïdes: tableau numpy
Collection de k centroïdes sous forme de tableau numpy.
"""
np.random.seed(random_state)
centroids = []
m = np.shape(C)[0]
for _ in range(k):
r = np.random.randint(0, m-1)
centroids.append(C[r])
return np.array(centroids)
def initialize_centroids(X, k):
"""renvoie k centroïdes à partir des points initiaux"""
centroids = X.copy()
np.random.shuffle(centroids)
return centroids[:k]
def kmeansplus_plus(C, k, random_state=13):
"""
Créez des centres de gravité de cluster à l'aide de l'algorithme K-Means++.
Paramètres
----------
ds: tableau numpy
Jeu de données à utiliser pour l'initialisation du centre de gravité.
k: int
Nombre souhaité de clusters pour lesquels des centres de gravité sont
requis.
Retour
-------
centroïdes: tableau numpy
Collection de k centroïdes sous forme de tableau numpy
Inspiration from here: https://stackoverflow.com/questions/5466323/how-
could-one-implement-the-k-means-algorithm
"""
np.random.seed(random_state)
centroids = [C[0]]
C])
for _ in range(1, k):
dist_sq = np.array([min([np.inner(c-x,c-x) for c in centroids]) for x in
probs = dist_sq/dist_sq.sum()
cumulative_probs = probs.cumsum()
r = np.random.rand()
for j, p in enumerate(cumulative_probs):
if r < p:
i = j
break
centroids.append(C[i])
return np.array(centroids)
# Online k-means algorithm using SGD
def online_kmeans(X, k):
""" K-signifie en ligne utilisant la descente de gradient stochastique.
X: matrice de données
C: centres initiaux
eta: 1/n_k diminue progressivement le taux d'apprentissage
"""
C = initialize_centroids(X,k)
cluster_etas = np.zeros(C.shape[0])
labels = []
for x in X:
j = np.argmin(((C - x)**2).sum(1))
cluster_etas [j] += 1
eta = 1.0/cluster_etas [j]
# update only the centroid with minimum distance
C[j] = (1.0 - eta) * C[j] + eta * x
labels.append(j)
#return C,np.array(labels),total_time
return C
# Fully online k-means algorithm
def fully_online(X, k):
"""
X: matrice de données
C: centres initiaux
f: coût de l'installation
"""
C = initialize_centroids(X, k+1)
n = k+1
dists = []
for x in C:
d = ((C - x)**2).sum(1)
d = [i for i in d if np.abs(i) > 1e-5]
dists.append(d)
j = np.min(dists)/2
f = j/k
r=1
q = 0
for x in X:
n += 1
D2 = np.min((C - x).sum(1))**2
p = np.min((D2/f, 1))
if np.random.random() < p:
C = np.append(C,np.array([x]), axis=0)
q += 1
if q >= 3*k*(1+np.log(n)):
r += 1
q = 0
f = 2*f
#return C, total_time
return C
def modified_fully_online(X, k_target):
"""
Algorithme modifié dans (Liberty et al.) Pour la conception expérimentale.
X: matrice de données
k_target: le nombre de clusters que nous voudrions que l'algorithme
produise
"""
k = (k_target - 15)/5
C = initialize_centroids(X, 10)
n = k+1
dists = []
for x in C:
d = ((C - x)**2).sum(1)
d = [i for i in d if np.abs(i) > 1e-5]
dists.append(d)
j = np.sum(sorted(dists)[:10])/2
f = j
r = 1
q = 0
for x in X:
n += 1
D2 = np.min((C - x).sum(1))**2
p = np.min((D2/f, 1))
if np.random.random() < p:
C = np.append(C, np.array([x]), axis=0)
q += 1
if q >= k:
r += 1
q = 0
f = 10*f
#return C, total_time
return C
