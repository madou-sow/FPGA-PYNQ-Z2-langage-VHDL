**BSP : modèle Bulk Synchronous Parallelism**

Le modèle BSP (Bulk Synchronous Parallelism) est un modèle de parallélisme bien adapté à l'utilisation des méthodes formelles. Il garantit une forme de structure dans le programme parallèle, en l'organisant en super-étapes où chacune d'entre elle est composées d'une phase de calculs, puis d'une phase de communications entre les unités de calculs.

BSML(Bulk-Synchronous Parallel ML) et DMML(Departmental Metacomputing ML) sont deux
extensions ML pour la programmation fonctionnelle d'algorithmes parallèles. Pour prédire le temps
d'exécution d'un programme BSML, il est nécessaire de connaître les paramètres BSP ainsi que la
puissance de calcul de la machine qui exécutera le programme.
Une bibliothèque BSMLlib généralisé comme un système de programmation des algorithmes
parallèles et globalisés,un algorithme pouvant être un serveur s'il entrelace deux ou plusieurs
algorithmes data-parallèles.

Il existe 4 paramètres BSP. Les paramètres g et L sont exprimés comme multiples de la vitesse des
processeurs r. Le paramètre de communication g et celui de synchronisation l sont obtenues en
mesurant le temps total d'une h-relation. Ces paramètres se mesurent en flops et sont dépendant du
paramètre r qui se mesure en Mflops/s. Une h-relation est une étape de communication où chaque
processeur envoie au h mots et reçoit au plus h mots et où au moins un processeur a reçu ou envoyé
h mots, un mot étant un réel ou un entier.

**Le Benchmark ou benchmarking**, désigne une technique de marketing visant pour une entreprise
à observer les performances d'une autre entreprise, à comparer et à analyser les performances de
produits ou services concurrents et leaders sur le marché, en vue d'optimiser la conception d'un
nouveau produit, plus ou moins ...
Le Benchmark est un outil de comparaison qui sert à évaluer la performance d’une entreprise sur
son secteur économique et la comparer aux meilleurs acteurs du secteur.
Cet outil d’amélioration continue se base sur un processus d’évaluation par rapport à un ou
plusieurs modèles reconnus.


## Temps d'exécution de la online_kmeans.py

fichier [online_kmeans.py](https://github.com/madou-sow/FPGA-PYNQ-Z2-langage-VHDL/blob/main/Init-Centroide-KmeansClustering/Benchmarks/code/online_kmeans.py)

## Benchmark sur la fonction online_kmeans.py
```
=== Méthode 1 ===
Durée d'exécution de la fonction online_kmeans avec la Méthode 1 en seconde =
1605786695.548345
[[ 9.44408823 -0.90708702]
[ 4.35926536 7.44593629]
[ 6.21332844 -5.574133 ]
[ 4.7753834 -4.89335503]]

=== Méthode 2 ===
Durée d'exécution de la fonction online_kmeans_centroids avec la Méthode 2 en
seconde = 1605786695.7001889

=== Méthode 3 ===
Execution time of online_kmeans avec la méthode 3 : 0.147717
[[ 2.23926755 5.56049828]
[ 5.90447535 9.87592788]
[ 7.07230502 8.74824861]
[ 7.48982647 -3.07190827]]

=== Méthode 4 ===
Execution time of online_kmeans_centroids avec la méthode 4 : 0.135914

=== Méthode 5 ===
[0.10423863300002267, 0.1126622009996936, 0.09649706700020033,
0.09639521900044201, 0.09585272100048314]

=== Méthode 6 ===
Function A starts the execution online_kmeans :
Function A completes the execution online_kmeans :
0.002914748999501171

=== Méthode 7 ===
Myfunction took 1.9073486328125e-06 seconds to complete its execution.

=== Méthode 8 ===
"online_kmeans" took 146.616 ms to execute
The sum of the first (array([[ 2.61827571, 4.7215674 ],
[ 8.14876823, -2.23589948],
[ 5.98895788, -6.10318594],
...,
[ 7.28781261, 9.70891356],
[ 5.73585917, 10.77364709],
[ 8.91511193, 9.82113604]]), 3) numbers is: [[ 4.35926536
[ 9.44408823 -0.90708702]
[ 5.5251141 -5.24830611]]
7.44593629]

=== Méthode 9 ===
Temps d'exécution "online_kmeans": 00:00:00.160 sec


=== Méthode 10 ===
Function "online_kmeans" took 0.14835279900034948 seconds to complete.
```

**Conversion d'un Code Python vers un Code C++**

[temps-execution-online-kmeans.py](https://github.com/madou-sow/FPGA-PYNQ-Z2-langage-VHDL/blob/main/Init-Centroide-KmeansClustering/code/temps-execution-online-kmeans.py) ==> [temps-execution-online-kmeans.cpp](https://github.com/madou-sow/FPGA-PYNQ-Z2-langage-VHDL/blob/main/Init-Centroide-KmeansClustering/code/temps-execution-online-kmeans.cpp)

### Compilation de kmeans.beautifier.cpp,kmeansPlusPlus.beautifier.cpp,main.beautifier.cpp en langage C avec Vivado HLS


<img alt="bitstream" src="https://github.com/madou-sow/FPGA-PYNQ-Z2-langage-VHDL/blob/main/images/exploration1.png" width=50% height=50%  title="Bits"/>

<img alt="bitstream" src="https://github.com/madou-sow/FPGA-PYNQ-Z2-langage-VHDL/blob/main/images/comp-debug.png" width=50% height=50%  title="Bits"/>
<img alt="bitstream" src="https://github.com/madou-sow/FPGA-PYNQ-Z2-langage-VHDL/blob/main/images/Resultat-compilation.png" width=50% height=50%  title="Bits"/>

```
Voici les résultats de la compilation avec VHLS
iteration 0 sum 876727
iteration 1 sum 529312
iteration 2 sum 264389
iteration 3 sum 40489.5
iteration 4 sum 15699.5
iteration 5 sum 9944.76
iteration 6 sum 11484.8
iteration 7 sum 18463.5
iteration 8 sum 42912.5
iteration 9 sum 40955.4
iteration 10 sum 19925.9
iteration 11 sum 6942.16
iteration 12 sum 2175.41
iteration 13 sum 2845.68
iteration 14 sum 4250.19
iteration 15 sum 3054.76
iteration 16 sum 1227.69
iteration 17 sum 983.915
iteration 18 sum 1691.66
iteration 19 sum 715.105
iteration 20 sum 316.992
iteration 21 sum 782.148
iteration 22 sum 2043.04
iteration 23 sum 755.202
iteration 24 sum 665.291
iteration 25 sum 648.511
iteration 26 sum 407.428
iteration 27 sum 305.98
iteration 28 sum 946.401
iteration 29 sum 1494.07
iteration 30 sum 2137.8
iteration 31 sum 1444.85
iteration 32 sum 3339.79
iteration 33 sum 4979.74
iteration 34 sum 5629.31
iteration 35 sum 5650.39
iteration 36 sum 4426.35
iteration 37 sum 2934.91
iteration 38 sum 2578.32
iteration 39 sum 2826.86
iteration 40 sum 2216.59
iteration 41 sum 2557.25
iteration 42 sum 860.549
iteration 43 sum 876.879
iteration 44 sum 0
calculate time 1.13162
Operation successfully performed
----------------- kmeans Plus Plus -----------------
iteration 0 sum 516522
iteration 1 sum 104513
iteration 2 sum 49736.7
iteration 3 sum 27383.9
iteration 4 sum 9389.86
iteration 5 sum 3785
iteration 6 sum 779.274
iteration 7 sum 0
calculate time 0.380654
Operation successfully performed


```
