## 22- Version Full FPGA avec PYNQ-Z2
A l'aide des Outils Vivado IP integrator, l'on va réaliser un simple additionneur complet (full adder) en
utilisant un langage de description matérielle : VHDL. Nous allons ensuite tester le full adder sur la carte
PYNQ-Z2 de la société XILINX. Les différentes étapes sont

- lancer l'outil  
- créer un nouveau projet  
- décrire un circuit combinatoire simpe en VHDL  
- créer un fichier de contraintes .xdc  
- faire une synthèse, le placement, le routage et la génération de bit stream  
- reconfigurer le circuit FPGA de la carte  
  
## 22.1- Qu'est-ce que c'est qu'un adder ou additionneur en Électronique
Un additionneur est un circuit numérique qui effectue l'addition de nombres. Dans de nombreux ordinateurs
et autres types de processeurs, des additionneurs sont utilisés dans les unités arithmétiques logiques ou ALU.
Ils sont également utilisés dans d'autres parties du processeur, où ils sont utilisés pour calculer des adresses,
des indices de table, des opérateurs d'incrémentation et de décrémentation et des opérations similaires.

Bien que les additionneurs puissent être construits pour de nombreuses représentations de nombres, telles
que les nombres décimaux codés en binaire ou en excès-3, les additionneurs les plus courants fonctionnent
sur des nombres binaires. Dans les cas où le complément à deux ou le complément à un est utilisé pour
représenter des nombres négatifs, il est trivial de modifier un additionneur en un additionneur-soustracteur.
D'autres représentations de nombres signés nécessitent plus de logique autour de l'additionneur de base.

## 22.2- Full adder (Additionneur complet)
**Additionneur complet**  
Un additionneur complet ajoute des nombres binaires et tient compte des valeurs reportées aussi bien en
entrée qu'en sortie. Un additionneur complet d'un bit ajoute trois nombres d'un bit, souvent écrits comme A,
B et Cin; A et B sont les opérandes, et Cin est un peu reporté de l'étape précédente moins significative.
L'additionneur complet est généralement un composant d'une cascade d'additionneurs, qui ajoutent des
nombres binaires de 8, 16, 32, etc. Le circuit produit une sortie à deux bits. Portée de sortie et somme
généralement représentées par les signaux Cout et S, où la somme est égale à 2Cout + S.

Un additionneur complet peut être implémenté de nombreuses manières différentes, par exemple avec un
circuit de niveau transistor personnalisé ou composé d'autres grilles. Un exemple d'implémentation est avec
**S = A ⊕ B ⊕ Cin et C B ⊕ B ⊕ Cin et C Cin et Cout = (A ⋅ B) + (C B) + (Cin ⋅ B) + (C (A ⊕ B ⊕ Cin et C B))**.

Dans cette mise en œuvre, la porte OU finale avant la sortie de report peut être remplacée par une porte XOR
sans modifier la logique résultante. L'utilisation de seulement deux types de portes est pratique si le circuit
est mis en œuvre en utilisant de simples puces de circuit intégré qui ne contiennent qu'un seul type de porte
par puce.

**NOR additionneur complet**  
Un additionneur complet peut également être construit à partir de deux demi-additionneurs en connectant A
et B à l'entrée d'un demi-additionneur, puis en prenant sa sortie de somme S comme l'une des entrées du
second demi-additionneur et Cin comme son autre entrée, et enfin les sorties de retenue des deux demi-
additionneurs sont connectées à une porte OU. La sortie de somme du second demi-additionneur est la sortie
de somme finale (S) de l'additionneur complet et la sortie de la porte OU est la sortie de retenue finale
(Cout). Le chemin critique d'un additionneur complet traverse les deux portes XOR et se termine au bit de
somme s. En supposant qu'une porte XOR prend 1 délais pour se terminer, le délai imposé par le chemin
critique d'un additionneur complet est égal à  

**T <sub>FA</sub> = 2 ⋅ B) + (C T  <sub>XOR</sub> = 2 D**

Le chemin critique d'une retenue passe par une porte XOR dans l'additionneur et par 2 portes (ET et OU)
dans le bloc de retenue et par conséquent, si les portes ET ou OU prennent 1 délai pour se terminer, a un
retard de  

**T  <sub>c</sub> = T  <sub>XOR</sub> + T  <sub>AND</sub> + T  <sub>or</sub> = D + D + D = 3 D**

La table de vérité pour l'additionneur complet est:
