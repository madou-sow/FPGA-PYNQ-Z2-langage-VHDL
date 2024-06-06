// -*- coding: utf-8 -*-
""" ;
Pour mesurer le temps d’exécution des fonctions ;
""" ;
try: ;
// importpsyco
// psyco.full()
// psycois no more maintened => pypy
#include "pypy.h"
except ImportError: ;
pass ;
#include "math.h"
#include "time.h"
#include "timeit.h"
#include "functools.h"
// ###1 et 2 : le temps d’exécution des fonctions : online_kmeans et
online_kmeans_centroids
temps = time.time() ;
online_kmeans(X, 3) ;
print ("\n=== Méthode 1 ===") ;
print ("Durée d'exécution de la fonction online_kmeans avec la Méthode 1 en
seconde = ", temps) ;
#include "math.h"
temps = time.time() ;
online_kmeans_centroids = onlink.online_kmeans(X, n_clusters) ;
print(online_kmeans_centroids) ;
print ("\n=== Méthode 2 ===") ;
print ("Durée d'exécution de la fonction online_kmeans_centroids avec la Méthode
2 en seconde = ", temps) ;
// ########3 et 4 : le temps d’exécution des fonctions : online_kmeans et
online_kmeans_centroids
measure_time(online_kmean) {
start = time.time() ;
online_kmeans(X, 3) ;
end = time.time() ;
elapsed = end - start ;
print ("\n=== Méthode 3 ===") ;
print ("Execution time of online_kmeans avec la méthode 3 : %f " %
elapsed) ;
measure_time(lambda:online_kmeans(X, 3)) ;
measure_time(online_kmeans_centroids) {
start = time.time() ;
online_kmeans_centroids = onlink.online_kmeans(X, n_clusters) ;
print(online_kmeans_centroids) ;
end = time.time() ;
elapsed = end - start ;
print ("\n=== Méthode 4 ===") ;
print ("Execution time of online_kmeans_centroids avec la méthode 4 : %f " %
elapsed) ;
measure_time(lambda:online_kmeans_centroids) ;
import_module = "import random" ;
testcode = ''' ;
online_kmeans(X,) {
""" Online k-means using stochastic gradient descent. ;
X : data matrix ;
C : initial centers ;
eta: 1/n_k gradually decreasing learning rate ;
""" ;
C = initialize_centroids(X,k) ;
cluster_etas = np.zeros(C.shape[0]) ;
labels = [] ;
for(index = 0;index < sizeof(X);index ++) { x = X[index];
j = np.argmin(((C - x)**2).sum(1)) ;
cluster_etas [j] += 1 ;
eta = 1.0/cluster_etas [j] ;
// update only the centroid with minimum distance
C[j] = (1.0 - eta) * C[j] + eta * x ;
labels.append(j) ;
// returnC,np.array(labels),total_time
}
return ( C ) ;
''' ;
print ("=== Méthode 5 ===") ;
print(timeit.repeat(stmt=testcode, setup=import_module)) ;
// ###Benchmark de la fonction online_kmeans
#include "timeit.h"
#include "time.h"
start_time = timeit.default_timer() ;
online_kmeans(X,) {
""" Online k-means using stochastic gradient descent. ;
X : data matrix ;
C : initial centers ;
eta: 1/n_k gradually decreasing learning rate ;
""" ;
C = initialize_centroids(X,k) ;
cluster_etas = np.zeros(C.shape[0]) ;
labels = [] ;
for(index = 0;index < sizeof(X);index ++) { x = X[index];
j = np.argmin(((C - x)**2).sum(1)) ;
cluster_etas [j] += 1 ;
eta = 1.0/cluster_etas [j] ;
// update only the centroid with minimum distance
C[j] = (1.0 - eta) * C[j] + eta * x ;
labels.append(j) ;
// returnC,np.array(labels),total_time
}
return ( C ) ;
print ("=== Méthode 6 ===") ;
print("Function A starts the execution online_kmeans :") ;
print("Function A completes the execution online_kmeans :") ;
print (timeit.default_timer() - start_time) ;
// ##Benchmark de la fonction online_kmeans avec un décorateur avec la fonction
timer_func et le module time
#include "random.h"
#include "time.h"
timer_func(func) {
function_timer(*args,) {
start = time.time() ;
value = func(*args, **kwargs) ;
end = time.time() ;
runtime = end - start ;
msg = "{func} took {time} seconds to complete its execution." ;
print ("\n=== Méthode 7 ===") ;
print(msg.format(func = func.__name__,time = runtime)) ;
return ( value ) ;
}
return ( function_timer ) ;
@timer_func ;
Myfunction() {
online_kmeans(X,) {
""" Online k-means using stochastic gradient descent. ;
X : data matrix ;
C : initial centers ;
eta: 1/n_k gradually decreasing learning rate ;
""" ;
C = initialize_centroids(X,k) ;
cluster_etas = np.zeros(C.shape[0]) ;
labels = [] ;
for(index = 0;index < sizeof(X);index ++) { x = X[index];
j = np.argmin(((C - x)**2).sum(1)) ;
cluster_etas [j] += 1 ;
eta = 1.0/cluster_etas [j] ;
// update only the centroid with minimum distance
C[j] = (1.0 - eta) * C[j] + eta * x ;
labels.append(j) ;
// returnC,np.array(labels),total_time
}
return ( C ) ;
if __name__ == '__main__': ;
Myfunction() ;
// ##Benchmark de la fonction online_kmeans avec un décorateur et avec le
module time
#include "functools.h"
#include "time.h"
timeit(my_func) {
@wraps(my_func) ;
timed(*args,) {
tstart = time.time() ;
output = my_func(*args, **kw) ;
tend = time.time() ;
print ("\n=== Méthode 8 ===") ;
print('"{}" took {:.3f} ms to execute\n'.format(my_func.__name__, (tend
- tstart) * 1000)) ;
return ( output ) ;
}
return ( timed ) ;
@timeit ;
online_kmeans(X,) {
""" Online k-means using stochastic gradient descent. ;
X : data matrix ;
C : initial centers ;
eta: 1/n_k gradually decreasing learning rate ;
""" ;
C = initialize_centroids(X,k) ;
cluster_etas = np.zeros(C.shape[0]) ;
labels = [] ;
for(index = 0;index < sizeof(X);index ++) { x = X[index];
j = np.argmin(((C - x)**2).sum(1)) ;
cluster_etas [j] += 1 ;
eta = 1.0/cluster_etas [j] ;
// update only the centroid with minimum distance
C[j] = (1.0 - eta) * C[j] + eta * x ;
labels.append(j) ;
// returnC,np.array(labels),total_time
}
return ( C ) ;
if __name__ == '__main__': ;
k=3 ;
print("The sum of the first {} numbers is: {}".format((X,k),
online_kmeans(X, k))) ;
// ##Benchmark de la fonction online_kmeans avec un décorateur et avec le module time
#include "functools.h"
#include "time.h"
#include "functools.h"
time_it(func) {
"""Timestamp decorator for dedicated functions""" ;
@functools.wraps(func) ;
wrapper(*args,) {
start = time.time() ;
result = func(*args, **kwargs) ;
elapsed = time.time() - start ;
mlsec = repr(elapsed).split('.')[1][:3] ;
readable = time.strftime("%H:%M:%S.{}".format(mlsec),
time.gmtime(elapsed)) ;
print ("\n=== Méthode 9 ===") ;
print('Temps d\'exécution "{}": {} sec'.format(func.__name__, readable))
;
return ( result ) ;
}
return ( wrapper ) ;
@time_it ;
online_kmeans(X,) {
""" Online k-means using stochastic gradient descent. ;
X : data matrix ;
C : initial centers ;
eta: 1/n_k gradually decreasing learning rate ;
""" ;
C = initialize_centroids(X,k) ;
cluster_etas = np.zeros(C.shape[0]) ;
labels = [] ;
for(index = 0;index < sizeof(X);index ++) { x = X[index];
j = np.argmin(((C - x)**2).sum(1)) ;
cluster_etas [j] += 1 ;
eta = 1.0/cluster_etas [j] ;
// update only the centroid with minimum distance
C[j] = (1.0 - eta) * C[j] + eta * x ;
labels.append(j) ;
// returnC,np.array(labels),total_time
}
return ( C ) ;
online_kmeans(X,k) ;
// ######Benchmark de la fonction online_kmeans avec la méthode de Jonathan
Kosgei et un decorateur simple
#include "timeit.h"
#include "functools.h"
timer(function) {
new_function() {
start_time = timeit.default_timer() ;
function() ;
elapsed = timeit.default_timer() - start_time ;
print ("\n=== Méthode 10 ===") ;
print('Function "{name}" took {time} seconds to
complete.'.format(name=function.__name__, time=elapsed)) ;
return ( new_function() ) ;
@timer ;
online_kmeans() {
""" Online k-means using stochastic gradient descent. ;
X : data matrix ;
C : initial centers ;
eta: 1/n_k gradually decreasing learning rate ;
""" ;
C = initialize_centroids(X,k) ;
cluster_etas = np.zeros(C.shape[0]) ;
labels = [] ;
for(index = 0;index < sizeof(X);index ++) { x = X[index];
j = np.argmin(((C - x)**2).sum(1)) ;
cluster_etas [j] += 1 ;
eta = 1.0/cluster_etas [j] ;
// update only the centroid with minimum distance
C[j] = (1.0 - eta) * C[j] + eta * x ;
labels.append(j) ;
// returnC,np.array(labels),total_time
}
return ( C ) ;
// ###############
