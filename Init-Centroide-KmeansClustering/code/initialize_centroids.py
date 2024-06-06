from math import sqrt, floor
import numpy as np
### fichier initialize_centroids.py
# https://gist.github.com/mmmayo13/3d5c2b12218dfd79acc27c64b3b7dd86
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
"""
def random(ds, k, random_state=42):
"""
Créez des centres de gravité de cluster aléatoires.
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
Collection de k centroïdes sous forme de tableau numpy.
"""
np.random.seed(random_state)
centroids = []
m = np.shape(ds)[0]
for _ in range(k):
r = np.random.randint(0, m-1)
centroids.append(ds[r])
return np.array(centroids)
def plus_plus(ds, k, random_state=42):
"""
Créez des centres de gravité de cluster à l'aide de l'algorithme k-means ++.
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
Collection de k centroïdes sous forme de tableau numpy.
Inspiration from here: https://stackoverflow.com/questions/5466323/how-
could-one-implement-the-k-means-algorithm
"""
np.random.seed(random_state)
centroids = [ds[0]]
for _ in range(1, k):
dist_sq = np.array([min([np.inner(c-x,c-x) for c in centroids]) for x in
ds])
probs = dist_sq/dist_sq.sum()
cumulative_probs = probs.cumsum()
r = np.random.rand()
for j, p in enumerate(cumulative_probs):
if r < p:
i = j
break
centroids.append(ds[i])
return np.array(centroids)
def naive_sharding(ds, k):
"""
Créez des centres de gravité de cluster à l'aide d'un algorithme de
partitionnement naïf déterministe.
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
Collection de k centroïdes sous forme de tableau numpy.
"""
def _get_mean(sums, step):
"""Vfunc vectorisable pour obtenir des moyennes de colonnes de fragments
additionnés."""
return sums/step
n = np.shape(ds)[1]
m = np.shape(ds)[0]
centroids = np.zeros((k, n))
composite = np.mat(np.sum(ds, axis=1))
ds = np.append(composite.T, ds, axis=1)
ds.sort(axis=0)
step = floor(m/k)
vfunc = np.vectorize(_get_mean)
for j in range(k):
if j == k-1:
centroids[j:] = vfunc(np.sum(ds[j*step:,1:], axis=0), step)
else:
centroids[j:] = vfunc(np.sum(ds[j*step:(j+1)*step,1:], axis=0),
step)
return centroids
