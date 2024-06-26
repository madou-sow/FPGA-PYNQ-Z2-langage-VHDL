## PandA (Bambu)

L'objectif principal du projet PandA est de développer un cadre utilisable qui permettra la recherche
de nouvelles idées dans le domaine de la co-conception HW-SW.
Le cadre PandA comprend des méthodologies soutenant la recherche sur la synthèse de haut niveau
des accélérateurs matériels, sur l'extraction de parallélisme pour les systèmes embarqués, sur le
partitionnement et le mappage matériel/logiciel, sur les métriques pour l'estimation des
performances des applications logicielles embarquées et sur les dispositifs reconfigurables
dynamiques.  
PandA est un logiciel libre, gratuit dans le sens où il respecte la liberté de l’utilisateur, publié sous la
licence publique générale GNU version 3 et en cours de développement à Politecnico di Milano
(Italie).  
Les fichiers sources actuellement distribués couvrent principalement la synthèse de haut niveau des
descriptions basées sur C/C ++. 

### 1- Bambu : synthèse de haut niveau pour la programmation parallèle

Les applications fonctionnant sur de très grands ensembles de données présentent des comportements uniques, tels que des accès mémoire imprévisibles et à granularité fine, et un parallélisme au niveau des tâches hautement déséquilibré, qui rendent les processeurs ou
accélérateurs polyvalents hautes performances existants (par exemple, les GPU) sous-optimaux.  
Pour résoudre ces problèmes, la recherche et l'industrie développent une variété de conceptions d'accélérateurs personnalisés pour ce domaine d'application, y compris des solutions basées sur des dispositifs reconfigurables (Field Programmable Gate Arrays). Ces nouvelles approches utilisent souvent la synthèse de haut niveau (HLS) pour accélérer le développement des accélérateurs. Ce tutoriel abordera l'impact des FPGA sur le calcul haute performance, en se concentrant sur les
applications dans les domaines de l'analyse de données et de l'apprentissage automatique. Le didacticiel plongera dans les approches de la synthèse de haut niveau (HLS) d'applications parallèles, mettant en évidence les méthodologies clés, les tendances, les avantages, les avantages, mais aussi les lacunes qui doivent encore être comblées. Le didacticiel fournira une expérience pratique de Bambu, l'un des outils HLS les plus avancés disponibles. Capable de prendre en charge
la majorité des constructions C, Bambu s'intègre à de nombreuses synthèses logiques et outils de simulation, générant des accélérateurs pour une variété de fournisseurs de FPGA, à partir de code
parallèle annoté avec OpenMP. Il optimise également les architectures mémoire des accélérateurs générés.

Résultat des tests avec Panda à partir de l’exploitation de la vectorisation à haut niveau Synthèse de boucles irrégulières imbriquées

### 2- Vectorisation des boucles externes en haut niveau La synthèse

- Les unités fonctionnelles vectorielles peuvent être synthétisées pour toutes les opérations de calcul  
- Avantages par rapport à la parallélisation complète de la boucle Machine à états finis plus simple  
    • Limite les frais généraux de la zone  
    • Limite la réduction de fréquence  

- Accès mémoire aligné  
    • Allocation de mémoire ad hoc  

- Les unités fonctionnelles vectorielles peuvent être obtenues par  
    • partage d'unités fonctionnelles scalaires  
    • réplication des unités fonctionnelles scalaires  

- Inconvénients  
Infrastructure de mémoire plus grande  
Unités fonctionnelles plus complexes

### 3- Premier exemple - Transformation de code

- Générez un accélérateur avec une taille de vecteur égale à un pour voir l'effet de la transformation du code

  <img alt="bambu-1" src="https://github.com/madou-sow/FPGA-PYNQ-Z2-langage-VHDL/blob/main/images/bambu1.png" width=70% height=70%  title="bambu-1"/>

  <img alt="bambu-2" src="https://github.com/madou-sow/FPGA-PYNQ-Z2-langage-VHDL/blob/main/images/bambu-2.png" width=70% height=70%  title="bambu-2"/>

  <img alt="bambu-3" src="https://github.com/madou-sow/FPGA-PYNQ-Z2-langage-VHDL/blob/main/images/bambu-3.png" width=70% height=70%  title="bambu-3"/>

<img alt="bambu-4" src="https://github.com/madou-sow/FPGA-PYNQ-Z2-langage-VHDL/blob/main/images/bambu-4.png" width=70% height=70%  title="bambu-4"/>
