## REPRÉSENTATION COMPORTEMENTALE DES SYSTÈMES NUMÉRIQUES

Dans le domaine des systèmes numériques, il existe deux grands domaines d’applications :
- les processeurs (et dérivés : microcontrôleurs, DSP...) qui font du traitement séquentiel
- les systèmes logiques qui font du traitement parallèle

  image

### Synthèse structurelle et description comportementale
Il existe deux moyens pour synthétiser un système numérique logique.
Le premier fait appel aux techniques de synthèse classique ou encore appelée synthèse structurelle. A partir
d’une table de vérité, on obtient les équations logiques des sorties, à partir des entrées, faisant intervenir des
opérateurs logiques .
Cette méthode permet d’obtenir la structure finale du système à concevoir. Chaque opérateur élémentaire
possède sa solution technologique sous forme de circuit intégré (circuits CMOS : 4001/porte XOR,
4081/porte ET, ...). Une fois la carte électronique réalisée, il n’est alors plus possible de modifier la fonction
réalisée.
Une autre méthode consiste à utiliser un composant logique programmable, laissant ainsi la possibilité de
modifier la fonction réalisée à souhait (mise à jour, correction de bugs...).
Il n’est alors plus nécessaire de connaître la structure que devra avoir le système final, mais de pouvoir
simplement son comportement. On parle alors de description comportementale du système. Ceci nécessite
l’utilisation de langage de description de haut niveau, tel que le VHDL ou le Verilog.

### Composants programmables
Il existe trois grandes catégories de systèmes logiques programmables :

- les CPLD (Complex Programmable Logic Device)
- les FPGA (Field Programmable Gate Array)
- les ASIC (Application Specific Integrated Circuit)

### Les FPGA
Ces systèmes programmables sont initialement destinés au prototypage de systèmes numériques
complexes. Ils sont une bonne alternative aux circuits spécifiques, les ASIC (Application Specific Integrated
Circuit), pour des petites ou moyennes séries.
Il existe plusieurs grands fabricants : ALTERA, ACTEL (composants spécialisés) et XILINX. Pour cette
expérience, nous utiliserons des FPGA de chez Xilinx.

#### Implantation
Chaque fabricant propose aussi des composants de taille variable : de 100.000 à 10.000.000 portes logiques.
Par comparaison, les portes standards commerciales possèdent entre 2 et 8 portes logiques pour une surface
de silicium quasiment identique.
Quelque soit la technologie utilisée, aucune porte logique n’est réellement implantée. Il s’agit en fait de
blocs logiques programmables, mais très versatiles (RAM), et d’une mer de connexions programmables.
Chez Xilinx, ces blocs logiques sont appelés CLB (Common Logic Blocks).

### Structure d’un FPGA - Xilinx
L’architecture, retenue par Xilinx, se présente sous forme de deux couches : une couche circuit configurable
et un réseau de mémoire SRAM. La structure d’un FPGA est donnée dans la figure suivante. L’échelle est
loin d’être réelle, les fonctions logiques n’occupant qu’environ 5% du circuit.

image

Les FPGA sont un rassemblement et une combinaison de différents blocs :

- d’entrées/sorties (IOB - Input Output Blocks),
- de routage (PSM - Programmable Switch Matrix),
- de logique programmable (CLB - Configurable Logic Blocks)
- et d’autres blocs plus spécifiques.

## DÉVELOPPEMENT D’UN SYSTÈME NUMÉRIQUE

Les langages de description de matériel (HDL = Hardware Description Langage) font partie des outils de
base pour la conception de systèmes logiques intégrés câblés, que le produit final soit construit sur des
composants électriquement configurables (FPGA = Field Programmable Logic Array) ou des circuits
intégrés spécifiques (ASIC = Application Specific Integrated Circuit).
Ces langages doivent être utilisables pour :

- écrire la spécification d’un système (description comportementale ou fonctionnelle)
- le construire par interconnexion de cellules élémentaires (description structurelle ou physique)
- gérer des description hiérarchisées (dont la description structurelle est un cas particulier)
- valider par simulation les différents types de description
- permettre l’utilisation de programmes de synthèse automatique
  
De plus les descriptions comportementales doivent se faire dans deux modes :

- mode concurrent : les données se propagent dans des éléments dont le comportement est décrit
par des déclarations qui ont un effet permanent (comme dans les descriptions structurelles)
- mode procédural : les données sont manipulées par des séquences d’instructions (comme dans
les programmes d’ordinateurs)

Dans le mode concurrent les données sont actives, on parle de “data flow”, alors que dans le mode
procédural c’est le programme qui contrôle les événements, on parle alors de “program flow”. Il existe deux
standards de langages de description de matériel :

- VHDL : Very High Speed integrated circuit Hardware Description Language ;
- Verilog : Le langage Verilog utilise deux classes de supports de données distinctes pour les modes
concurrents et procédural.
- classe “net” dans le mode concurrent : un net est équivalent à un noeud d’un circuit électrique, son état est
contrôlé en permanence par les éléments aux sorties desquels il est connecté.
- classe “reg” dans le mode procédural : un reg est équivalent à une variable d’un programme informatique :
il subit des affectations instantanées par instructions et conserve son état jusqu’à la prochaine affectation.
Leurs syntaxes sont assez différentes mais mettent en oeuvre les mêmes concepts.

Nous nous intéresserons par la suite au VHDL, qui est un langage de description normalisé (IEEE) et quasi-
universel pour décrire des circuits intégrés.
