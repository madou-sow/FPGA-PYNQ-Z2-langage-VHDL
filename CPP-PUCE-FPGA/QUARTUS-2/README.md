## Logiciel Quartus II
Le logiciel de développement Quartus II fournit un environnement de conception complet pour la
conception de système sur puce programmable (SOPC). Que vous utilisiez un ordinateur personnel
ou une station de travail Linux, le logiciel Quartus II garantit une saisie facile de la conception, un
traitement rapide et une programmation simple des appareils. Les sections suivantes décrivent les
capacités générales et les flux de conception du logiciel Quartus II.

### 1- Quartus II Points forts:
Le logiciel Quartus II offre une interface utilisateur graphique riche complétée par un système
d'aide en ligne illustré et facile à utiliser. Le système Quartus II complet comprend un
environnement de conception intégré qui comprend chaque étape de la conception à la
programmation de l'appareil.

Vous pouvez facilement combiner différents types de fichiers de conception dans un projet
hiérarchique, en choisissant le format d'entrée de conception qui fonctionne le mieux pour chaque
bloc fonctionnel. Vous pouvez utiliser l'éditeur de blocs Quartus II pour créer des schémas
fonctionnels décrivant votre conception à un niveau supérieur, puis utiliser des schémas
fonctionnels supplémentaires, des schémas, des fichiers de conception de texte AHDL (.tdf), des
fichiers d'entrée EDIF (.edf), des fichiers de conception VHDL. (.vhd) et Verilog HDL Design Files
(.v) pour créer les composants de conception de niveau inférieur. L'entrée de conception
indépendante de l'architecture vous donne la liberté de créer une logique sans vous soucier de la
mise en œuvre finale de l'appareil.

L'interface utilisateur avancée du logiciel Quartus II vous permet de travailler avec plusieurs
fichiers en même temps, d'éditer plusieurs fichiers de conception pour transférer des informations
entre eux, tout en compilant ou simulant simultanément un autre projet. Vous pouvez afficher toute
une hiérarchie de fichiers de conception et passer en douceur d'un niveau hiérarchique à un autre.
Lorsque vous ouvrez un fichier de conception, le logiciel Quartus II démarre automatiquement
l'éditeur de conception approprié.

Le compilateur Quartus II est au cœur du système, fournissant un traitement de conception puissant
que vous pouvez personnaliser pour obtenir la meilleure implémentation silicium possible de votre
projet. La localisation automatique des erreurs et une documentation complète sur les messages
d'erreur et d'avertissement rendent les modifications de conception aussi simples que possible. À
chaque étape du processus de conception, le logiciel Quartus II vous permet de vous concentrer
facilement sur votre conception et non sur l'utilisation du logiciel.

La superbe intégration du logiciel Quartus II améliore votre efficacité et votre productivité, vous donnant le contrôle de votre environnement de conception logique.

### 2- Développer les capacités de conception :


Le logiciel Quartus II est un progiciel entièrement intégré et indépendant de l'architecture pour la conception de logique avec des dispositifs logiques programmables (PLD) Altera, notamment Arria
II, Arria GX, Arria V, Cyclone, Cyclone II, Cyclone III, Cyclone IV, Cyclone V, HardCopy II,
HardCopy III, HardCopy IV, MAX II, MAX V, MAX 3000A, MAX 7000AE, MAX 7000B, MAX
7000S, Stratix, Stratix II, Stratix II GX, Stratix III, Stratix IV, Stratix V et Stratix GX. Le logiciel Quartus.
``` 
II offre une gamme complète de capacités de conception logique:
  - Entrée de conception à l'aide de schémas, de schémas fonctionnels, AHDL, VHDL et Verilog HDL
  - Modification du plan d'étage
  - Conception incrémentielle LogicLock
  - Synthèse logique puissante
  - Simulation fonctionnelle et temporelle
  - Analyse du timing
  - Analyse logique intégrée avec l'analyseur logique SignalTap II
  - Importation, création et liaison de fichiers source de logiciels pour produire des fichiers de programmation
  - Projets combinés de compilation et de logiciels
  - Localisation d'erreur automatique
  - Programmation et vérification des appareils
```
### 3- À propos de la synthèse 

Vous pouvez utiliser le module Analyse et synthèse du compilateur pour analyser et synthétiser les
fichiers de conception et créer la base de données du projet. Analysis & Synthesis effectue une
synthèse logique pour minimiser l'utilisation logique de la conception et effectue un mappage
technologique pour implémenter la logique de conception en utilisant des ressources de
périphérique telles que des éléments logiques. Enfin, Analysis & Synthesis génère une base de
données de projet unique intégrant tous les fichiers de conception dans une conception.

Analysis & Synthesis utilise la synthèse intégrée Quartus II pour synthétiser vos fichiers Verilog
Design Files (.v) ou VHDL Design Files (.vhd). Vous pouvez utiliser d'autres outils de synthèse
EDA pour synthétiser vos fichiers de conception Verilog ou vos fichiers de conception VHDL, puis
générer un fichier netlist EDIF (.edf) ou un fichier de mappage Verilog Quartus (.vqm) que vous
pouvez utiliser avec le logiciel Quartus II.

Vous pouvez démarrer une compilation complète, qui comprend le module Analyse et synthèse, ou
vous pouvez démarrer Analyse et synthèse avec la commande Démarrer l'analyse et la synthèse
pour une conception. Le logiciel Quartus II vous permet également d'effectuer une analyse et une
élaboration pour vérifier les fichiers de conception à la recherche d'erreurs de syntaxe et de
sémantique, ou d'utiliser la commande Analyser le fichier actuel pour rechercher des erreurs de
syntaxe dans un seul fichier de conception. Ces commandes n'effectuent pas de synthèse logique ou
de mappage technologique sur la logique de conception.

### 4- Simulation de conceptions 

La simulation vérifie le comportement de la conception avant de programmer un appareil. Le
logiciel Quartus II prend en charge et intègre les simulateurs RTL standard et EDA au niveau de la
porte. La simulation RTL est une vérification précise du cycle de votre code source HDL et des
modèles de simulation fournis par Altera et d'autres fournisseurs IP. La simulation au niveau de la porte vérifie la fonctionnalité d'une conception après synthèse (netlist fonctionnelle post-synthèse), après synthèse et ajustement (netlist fonctionnelle post-ajustement), ou après analyse temporelle (netlist temporel post-ajustement).

La simulation des conceptions Altera implique la configuration de l'environnement de travail du
simulateur, la compilation de bibliothèques de modèles de simulation et l'exécution de votre
simulateur. Le logiciel Quartus II prend en charge les flux de simulation automatisés et
personnalisés.


### 5- Développer la sélection de l'appareil et les ressources utilisées par la conception

Différentes familles d'appareils ont des caractéristiques de puissance différentes. Des paramètres tels que la technologie de processus, la tension d'alimentation, la conception électrique et l'architecture de l'appareil affectent tous la consommation d'énergie. Au sein des familles d'appareils, les appareils plus gros consomment souvent plus d'énergie que les appareils plus petits.
Le choix de l'ensemble de l'appareil affecte également la capacité de l'appareil à dissiper la chaleur et peut influencer la solution de refroidissement requise. Dans tous les cas, vous devez consulter les spécifications de l'appareil pour obtenir des informations sur les caractéristiques d'alimentation de cet appareil.
Les familles d'appareils Stratix III, Stratix IV et Stratix V intègrent la Programmable Power
Technology, une architecture avancée qui offre un équilibrage spécifique de la vitesse et de la
puissance. La technologie d'alimentation programmable peut réduire considérablement la puissance
statique et peut réduire légèrement la puissance dynamique.

Les conceptions qui utilisent plus de ressources ont tendance à consommer plus d'énergie que les
conceptions qui utilisent moins de ressources. Les facteurs pertinents sont les suivants:
Le nombre, le type et le chargement des broches d'E/S. Les broches de sortie entraînant des
composants hors puce consomment généralement une puissance dynamique accrue pour chaque
transition. Les normes d'E/S terminées par des résistances externes tirent généralement de l'énergie statique de la broche de sortie.
Le nombre d'éléments logiques, de multiplicateurs et d'éléments de RAM utilisés, ainsi que leurs
modes de fonctionnement, affectent tous la consommation d'énergie.
Le nombre et le type de signaux globaux couvrant de grandes zones de l'appareil peuvent avoir
une consommation d'énergie dynamique significative.
