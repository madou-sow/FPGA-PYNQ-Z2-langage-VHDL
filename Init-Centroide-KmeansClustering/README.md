## Les Méthodes d'initialisation des Centroïdes pour du KMeans Clustering

Nous allons exploiter la méthode de travail Matthew Mayo pour élaborer une version "Full FPGA" de
Clustering. Pour cela nous allons nous approprier ce programme et l'implémenter pour arriver à fin. Les
Méthodes de Clustering telles que KMeans permettent de savoir comment aborder correctement un problème
d'apprentissage non supervisé.

Nous allons examiner quelques aspects d'une chaîne de traitement avec KMeans Clustering. Nous parlerons
de l'initialisation avec des centres de gravité en détaillant certaines approches. La programmation est faite en
python.

### 1- KMeans Clustering

KMeans est une approche simple, mais souvent efficace, du clustering. Traditionnellement, k points de
données d'un ensemble de données donné sont choisis au hasard comme centres de cluster, ou centres de
gravité, et toutes les instances d'entraînement sont tracées et ajoutées au cluster le plus proche. Une fois que
toutes les instances ont été ajoutées aux clusters, les centroïdes, représentant la moyenne des instances de
chaque cluster, sont recalculés, ces centroïdes recalculés devenant les nouveaux centres de leurs clusters
respectifs.  
À ce stade, toutes les appartenances au cluster sont réinitialisées et toutes les instances de l'ensemble
d'apprentissage sont de nouveau tracées et ajoutées à leur cluster le plus proche, éventuellement recentré. Ce
processus itératif se poursuit jusqu'à ce qu'il n'y ait pas de changement dans les centres de gravité ou leur
appartenance, et les clusters sont considérés comme réglés.
La convergence est obtenue une fois que les centres de gravité recalculés correspondent aux centres de
gravité de l'itération précédente ou se trouvent dans une marge prédéfinie.

### 2- Méthode d'initialisation du Centre de Gravité

Comme le KMeans Clustering vise à converger vers un ensemble optimal de centres de cluster (centroïde) et
d'appartenance au cluster en fonction de la distance de ces centroïdes via des itérations successives, il est
intuitif que plus le positionnement de ces centroïdes initiaux est optimal, moins il y a d'itérations du KMeans
que les algorithmes de Clustering seront nécessaire pour la convergence.  

Nous allons nous concentrer à quelques méthodes d'initialisation du centre de gravité : 
- **points de données aléatoires** : dans cette approche k points de données aléatoires sont sélectionnés dans
l'ensemble de données et utilisés comme centroïdes initiaux, elle fournit un scénario où les centroïdes
sélectionnés ne sont pas bien positionné dans tout l'espace de données  
- **KMeans++** : L'algorithme a pour objectif d'étaler les centres de gravité initiaux, il le fait en attribuant le
premier centre de gravité à l'emplacement d'un point de données sélectionné au hasard, puis en choisissant
les centres de gravité suivants à partir des données restants sur une probabilité proportionnelle à la distance
au carré du centre de gravité existant le plus proche d'un point donné  
- **Naïf-Sharding** : Cette méthode dépend du calcul d'une valeur de sommation composite reflétant toutes les
valeurs d'attribut d'une instance. Une fois cette valeur composite calculée, elle est utilisée pour trier les
instances de l'ensemble de données. le jeu de données est ensuite divisé horizontalement en k morceaux,
fragments. Enfin, les attributs d'origine de chaque partition sont additionnés indépendamment, leur moyenne
est calculée et la collection résultante de lignes de valeurs moyennes d'attributs de partition devient
l'ensemble des centres de gravité à utiliser pour l'initialisation. On s'attend à ce que, en tant que méthode
déterministe, elle fonctionne beaucoup plus rapidement que les méthodes stochastiques et se rapproche de la dispersion des centres de gravité initiaux dans l'espace de données via la valeur de sommation composite.

Vous pouvez sélectionner au hasard n'importe où dans l'espace de données, par opposition uniquement à
l'espace qui contient des points de données existants; vous pouvez essayer de trouver d'abord le point de
données le plus central, par opposition à une sélection aléatoire, et procéder avec K-Means ++ à partir de là;
vous pouvez échanger l'opération moyenne post-sommation pour une alternative dans le partitionnement
naïf.

### 2.1- Initialisation Centroïd et Scikit-Learn

Nous utiliserons Scikit-Learn pour effectuer notre Clustering :


### 2.2- Méthode d'initialisation du centre de gravité disponibles :

- 'KMeans ++': sélectionne les centres de cluster initiaux pour le Clustering KMeans de manière
intelligente pour accélérer la convergence.  
- 'Random': choisissez n_clusters observations (lignes) au hasard à partir des données des centres de gravité initiaux.  
- Si un ndarray est passé, il doit être de forme (n_clusters, n_features) et donner les centres initiaux.  
- Si un appel est passé, il doit prendre les arguments X, n_clusters, un état aléatoire et retourner une initialisation.
  
Notre objectif est de comparer et inspecter les centres de gravité initialisés :  
- Nous ne pouvons pas le faire avec les implémentations de Scikit-Learn  
- Nous utiliserons nos propres implémentations des 3 méthodes discutées ci-dessus, à savoir
l'initialisation aléatoire des centroïdes, K-Means ++ et partitionnement naïf.  
- Nous utiliserons nos implémentations indépendantes de Scikit-Learn pour créer nos centres de
gravité et les transmettre en tant que ndarray au moment du Clustering  
- nous pouvons également utiliser l'option callable, par opposition à l'option ndarray, et intégrer l'initialisation du centroïde dans l'exécution de K-Means Scikit-Learn, mais cela nous ramène à la case départ avec l'impossibilité d'examiner et de comparer ces centroïdes avant le Clustering  
- Cela dit, le fichier initialize_centroids.py contient nos implémentations d'initialisation centroïde avec les fonctions :  
- random : pour générer des centres de gravité de cluster aléatoires  
- plus_plus : pour générer des centres de gravité de cluster à l'aide de l'algorithme KMeans ++
naive_sharding : pour générer des centres de gravité de cluster à l'aide d'un algorithme de
partitionnement naïf déterministe  
- _ get _ mean : Vfunc vectorisable pour obtenir des moyennes de colonnes de fragments additionnés


fichier [initialize_centroids.py](https://github.com/madou-sow/FPGA-PYNQ-Z2-langage-VHDL/blob/main/Init-Centroide-KmeansClustering/code/initialize_centroids.py)

Le fichier onlin_kmeans.py contient des fonctions que nous allons importer et exploiter les 3 méthodes instanciations de l'algorithme KMeans :  

- online_kmeans : K-Means en ligne utilisant la descente de gradient stochastique  
- fully_online
- et modified_fully_online

Avec ce fichier placé dans le même répertoire que celui où j'ai démarré le Notebook Jupyter, je peux procéder comme suit, en commençant par les importations des bibliothèques et en utilisant le module **onlin_kmeans** à la place de **sklearn.cluster**  

```
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#from sklearn.cluster import KMeans
import onlin_kmeans as onlink
#import initialize_centroids as init_cent
%matplotlib inline
```

## 3- Création de certaines données

De toute évidence, nous aurons besoin de certaines données. Nous allons créer un petit ensemble synthétique
afin d'avoir le contrôle sur la délimitation claire de nos grappes (voir Figure 1).

```
from sklearn.datasets import make_blobs
n_samples = 250
n_features = 2
n_clusters = 4
random_state = 13
max_iter = 100
X, y = make_blobs(n_samples=n_samples,
n_features=n_features,centers=n_clusters,random_state=random_state)
fig=plt.figure(figsize=(8,8), dpi=80, facecolor='w', edgecolor='k')
plt.scatter(X[:, 0], X[:, 1]);

```

## 4- Initialisation des centroïdes

## 4.1- Initialisation aléatoire avec le Module onlink
```
random_centroids = onlink.random(X, n_clusters)
print(random_centroids)

[[ 5.00747147 -4.95714911]
[ 5.75351227 9.89013493]
[ 4.62571299 -6.02383563]
[ 9.65359174 -1.09605057]]

``` 
## 4.2- Initialisation Controïde avec la fonction initialize_centroids
```
initialize_centroids(X, 3)

array([[10.1605468 , -1.9134754 ],
[ 3.43797499, 5.69301239],
[ 5.95128954, -6.76202071]])
``` 
## 4.3- Initialisation de la fonction online_kmeans
```
Methode 1  
online_kmeans(X, 3)
array([[ 9.45183855, -0.75595106],
[ 4.23638917, 7.34437084],
[ 5.47389162, -5.26687277]])

Methode 2
online_kmeans_centroids = onlink.online_kmeans(X, n_clusters)
print(online_kmeans_centroids)
[[ 5.43772119 -5.29039364]
[ 9.24308503 -1.00831402]
[ 6.319311
9.20703104]
[ 2.11987182 5.45166773]]
``` 
## 4.4- Tracé des centroïdes avec la fonction online_kmeans
```
plt.scatter(X[:, 0], X[:, 1])
centroids = online_kmeans(X, 3)
plt.scatter(centroids[:, 0], centroids[:, 1],c='r', s=100)
<matplotlib.collections.PathCollection at 0x7f913cdc3490>
``` 

## 4.5- Initialisation avec la fonction modified_fully_online

```
Methode 1

modified_fully_online(X, 3)
array([[ 6.19393218, -3.19548236],
[ 7.03273395, -6.29455273],
[ 8.58500677, -0.55985579],
[ 9.80523306, -1.82230884],
[ 9.12834325, -1.04247409],
[ 3.4924673 , 4.2556699 ],
[ 2.29247953, 5.7935208 ],
[ 3.94356355, 4.43644954],
[ 4.53704619, -5.77616485],
[ 7.44860203, 7.38710623]])

Methode 2

modified_fully_online_centroids = onlink.modified_fully_online(X, n_clusters)
print(modified_fully_online_centroids)
[[11.16919824 -0.15316666]
[ 2.29247953 5.7935208 ]
[ 4.93306851 -5.70292798]
[ 0.20343155 7.74917905]
[ 9.42135429 -1.81247762]
[ 5.00747147 -4.95714911]
[ 1.98433261 5.2456394 ]
[ 3.08093425 6.39956266]
[ 9.25780094 -0.34322652]
[ 6.02012917 9.71546134]]
``` 
