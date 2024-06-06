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
