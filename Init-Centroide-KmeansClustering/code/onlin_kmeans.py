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
