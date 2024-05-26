## I. REPRÉSENTATION COMPORTEMENTALE DES SYSTÈMES NUMÉRIQUES

Dans le domaine des systèmes numériques, il existe deux grands domaines d’applications :
- les processeurs (et dérivés : microcontrôleurs, DSP...) qui font du traitement séquentiel
- les systèmes logiques qui font du traitement parallèle

 <img alt="numerique" src="https://github.com/madou-sow/FPGA-PYNQ-Z2-langage-VHDL/blob/main/images/schema-systeme-numerique.png" width=50% height=50%  title="numerique"/>

### 1. Synthèse structurelle et description comportementale
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

### 2. Composants programmables
Il existe trois grandes catégories de systèmes logiques programmables :

- les CPLD (Complex Programmable Logic Device)
- les FPGA (Field Programmable Gate Array)
- les ASIC (Application Specific Integrated Circuit)

### 3. Les FPGA
Ces systèmes programmables sont initialement destinés au prototypage de systèmes numériques
complexes. Ils sont une bonne alternative aux circuits spécifiques, les ASIC (Application Specific Integrated
Circuit), pour des petites ou moyennes séries.
Il existe plusieurs grands fabricants : ALTERA, ACTEL (composants spécialisés) et XILINX. Pour cette
expérience, nous utiliserons des FPGA de chez Xilinx.

#### 3.1 Implantation
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

 <img alt="fpga" src="https://github.com/madou-sow/FPGA-PYNQ-Z2-langage-VHDL/blob/main/images/structureFPGA.png" width=50% height=50%  title="fpga"/>

Les FPGA sont un rassemblement et une combinaison de différents blocs :

- d’entrées/sorties (IOB - Input Output Blocks),
- de routage (PSM - Programmable Switch Matrix),
- de logique programmable (CLB - Configurable Logic Blocks)
- et d’autres blocs plus spécifiques.

## II. DÉVELOPPEMENT D’UN SYSTÈME NUMÉRIQUE

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

### 1. Phases de développement

 <img alt="phase" src="https://github.com/madou-sow/FPGA-PYNQ-Z2-langage-VHDL/blob/main/images/phase-developpement-syst-num.png" width=70% height=70%  title="phase"/>

 L’écriture du module VHDL est la première chose à réaliser. Ensuite, il est possible (et fortement conseillé)
de vérifier la syntaxe de la description, en faisant appel à la fonction **Check Syntax** dans la partie
**Synthesis XST**. Cette étape est assez rapide et ne nécessite pas de connaître la cible, contrairement à
l’étape d’après. Viens ensuite la phase de synthèse ("Synthesis XST") puis de placement et de routage
("Implement Design"). Ces étapes nécessitent la connaissance, d’une part, de la cible (FPGA ou CPLD) et,
d’autre part, de l’environnement du circuit (entrées/sorties associées aux autres composants de la maquette).
Il est donc nécessaire, avant de réaliser ces étapes-là, de faire l’assignation des broches du composant avec la
description fournie. Pour cela, vous pouvez vous aider de la fonction "Assign Package Pins" dans la partie
"User Constraints" et de la documentation de la maquette fournie en début de ce document.


 <img alt="phase" src="https://github.com/madou-sow/FPGA-PYNQ-Z2-langage-VHDL/blob/main/images/maquette-generation-bitstream.png" width=70% height=70%  title="phase"/>

### 2. Structure d’un module VHDL

La description d’un système numérique par le biais du langage VHDL passe par 3 étapes différentes :
- la déclaration des ressources externes (bibliothèques) ;
- la description de l’entité du système, correspondant à la liste des entrées/sorties ;
- la description de l’architecture du système, correspondant à la définition des fonctionnalités du système.
L’ensemble est contenu dans un fichier source portant l’extension *.vhd.

#### 2.1. Déclaration des ressources externes

Cette phase est réalisée automatiquement pour les bibliothèques courantes. On retrouve en en-tête du fichier
source *.vhd les instructions suivantes :

```
1 library IEEE ;
2 use IEEE . STD_LOGIC_1164 . ALL;
3 use IEEE . STD_LOGIC_ARITH . ALL;
4 use IEEE . STD_LOGIC_UNSIGNED . ALL;
```

#### 2.2. Entité

L’entité permet de spécifier les différents ports d’entrées/sorties du système. Pour
chacun d’entre eux, il est indispensable de donner sa direction :
- in entrée simple
- out sortie simple
- buffer sortie rétroactive
- inout entrée-sortie bidirectionnelle (conflits possibles) et son type (voir section suivante).

   <img alt="vhdl" src="https://github.com/madou-sow/FPGA-PYNQ-Z2-langage-VHDL/blob/main/images/schema-entite-vhdl.png" width=50% height=50%  title="vhdl"/>

```
1 entity cours is
2 port (
3      a, b : in STD_LOGIC ;
4      s : out STD_LOGIC
5 );
6 end cours ;
```

#### 2.3. Architecture

Une architecture est reliée à une entité et permet de décrire le fonctionnement du système. Cette description
peut être de deux types :
- description comportementale : le comportement du système est décrit (description la plus couramment
utilisée en VHDL) ;
- description structurelle : la structure même du système est décrite à base de portes logiques, bascules...(description réservée à des fonctions simples ou pré-calculées).

```
1 architecture Behavorial of cours i s
2 −− declaration dessignaux
3 begin
4    processus1 ;
5    processus2 ;
6    ...
7 end Behavorial ;
```

### 3. Objets et types en VHDL

#### 3.1. Objets

- signal objet physique, associé à des évènements
- variable intermédiaire de calcul, non physique
- constant

#### 3.2. Types

Types de base : **bit, bit_vector, integer, boolean**

Types IEEE : **std_logic, std_logic_vector, signed, unsigned**

Types définis par l’utilisateur :
- type énuméré, exemple : type jour is **(lu, ma, me, je, ve, sa, di)**; (souvent utilisé dans les machines à état)
- sous-type : **subtype octet is bit_vector(0 to 7);**

#### 3.3. Notations

bit : ’0’ ou ’1’ ; bit_vector : "0100" ; ASCII : "Texte" ; Décimal : 423 ;

Hexadécimal : x"1A"

#### 3.4. Opérateurs en VHDL

LOGIQUES : and, nand, or, nor, xor, xnor, not

DÉCALAGE : sll, slr, sla, sra, rol, ror

RELATIONNELS : =, /=, <, >, <=, >=

ARITHMÉTIQUES : +, -, *, /, MOD

CONCATENATION : &

AFFECTATION : <=
