Le dispositif programmable Xilinx® Zynq® All est un SOC basé
- sur un processeur ARM® Cortex®-A9 double coeur (appelé système de traitement ou PS),
- intégré au tissu FPGA (appelé logique programmable ou PL).

Le sous-système PS comprend
- un certain nombre de périphériques dédiés (contrôleurs de mémoire, USB, UART, IIC, SPI, etc.)
- et peut être étendu avec une IP matérielle supplémentaire dans une superposition PL.

Les superpositions, ou bibliothèques matérielles, sont des conceptions FPGA programmables/configurables
qui étendent l'application utilisateur du système de traitement du Zynq à la logique programmable. Les
superpositions peuvent être utilisées pour accélérer une application logicielle ou pour personnaliser la plateforme matérielle pour une application particulière.

Un programmeur de logiciel peut utiliser une superposition d'une manière similaire à une bibliothèque de
logiciels pour exécuter certaines des fonctions de traitement d'image (par exemple, détection de bord,
seuillage, etc.) sur la structure FPGA. Les superpositions peuvent être chargées dynamiquement sur le
FPGA, selon les besoins, tout comme une bibliothèque de logiciels. Dans cet exemple, des fonctions de
traitement d'image distinctes pourraient être implémentées dans différentes superpositions et chargées à partir de Python à la demande.

PYNQ fournit une interface Python pour permettre aux superpositions dans le PL d'être contrôlées à partir de Python s'exécutant dans le PS. La conception FPGA est une tâche spécialisée qui nécessite des connaissances
et une expertise en ingénierie matérielle. Les superpositions PYNQ sont créées par des concepteurs de
matériel et encapsulées avec cette API PYNQ Python. Les développeurs de logiciels peuvent ensuite utiliser l'interface Python pour programmer et contrôler des superpositions de matériel spécialisé sans avoir à concevoir eux-mêmes une superposition. Ceci est analogue aux bibliothèques de logiciels créées par des développeurs experts qui sont ensuite utilisées par de nombreux autres développeurs de logiciels travaillant, au niveau de l'application.

**SOC (System On a Chip)** : Traduit littéralement en français par système sur une puce, un SOC, désigne un
circuit intégré qui regroupe, sur une seule et unique puce, les différents composants d'un ordinateur tels que les processeurs, la mémoire, les périphériques d'interface, etc.

**IP** : Propriété Intellectuel => Intelectual Property

**PL** : Programmation Logique

**PS** : Programmation Système

**Overlay** : Superposition

## 1- CHARGEMENT D'UNE SUPERPOSITION (Loading an Overlay)

Par défaut, un overlay (bitstream) appelé base est téléchargé dans PL au démarrage. La superposition de base
peut être considérée comme une conception de référence pour une planche. De nouvelles superpositions
peuvent être installées ou copiées sur la carte et peuvent être chargées dans le PL pendant que le système
fonctionne.

Une superposition comprend généralement:
- Un bitstream pour configurer la structure FPGA
- Un fichier Tcl de conception Vivado pour déterminer l'adresse IP disponible
- API Python qui expose les adresses IP en tant qu'attributs

La classe PYNQ Overlay peut être utilisée pour charger une superposition. Une superposition est instanciée
en spécifiant le nom du fichier de flux binaire. L'instanciation de la superposition télécharge également le
flux binaire par défaut et analyse le fichier Tcl.

## 2- Superpositions PYNQ-Z2 (Overlays PYNQ-Z2)

La carte PYNQ-Z2 présente les caractéristiques suivantes: Spécification de produit : ZYNQ XC7Z020-
1CLG400C

- Processeur Cortex-A9 bicoeur à 650 MHz
- Contrôleur de mémoire DDR3 avec 8 canaux DMA et 4 ports esclaves AXI3 hautes performances
- Contrôleurs de périphériques à large bande passante: 1G Ethernet, USB 2.0, SDIO
- Contrôleur de périphérique à faible bande passante: SPI, UART, PEUT, I2C
- Programmable à partir de JTAG, flash Quad-SPI, et carte MicroSD
- Logique programmable équivalente à l'Artix-7 FPGA
- 13 300 tranches logiques, chacune avec quatre LUT à 6 entrées et 8 tongs
- 630 Ko de RAM bloc rapide
- 4 tuiles de gestion d'horloge, chacune avec une phase boucle verrouillée (PLL) et horloge en mode mixte
gestionnaire (MMCM)
- 220 tranches DSP
- Convertisseur analogique-numérique sur puce (XADC) Mémoire
- 512 Mo de mémoire DDR3 avec bus 16 bits à 1050 Mbps
- Flash Quad-SPI 16 Mo avec programmation d'usine Compatible EUI-48/64 ™ 48 bits unique au monde
identifiant
- Emplacement MicroSD Puissance
- Alimenté par une source d'alimentation externe USB ou 7V-15V
- Gigabit Ethernet PHY
- Circuit de programmation micro USB-JTAG
- Pont micro USB-UART
- USB 2.0 OTG PHY (prend en charge l'hôte uniquement) Audio et vidéo
- Port récepteur HDMI (entrée)
- Port source HDMI (sortie)
- Interface I2S avec DAC 24 bits avec prise TRRS 3,5 mm
- Entrée ligne avec prise jack 3,5 mm Interrupteurs, boutons poussoirs et LED
- 4 boutons poussoirs
- 2 interrupteurs à glissière
- 4 LED
- 16 E/S FPGA totales (8 broches partagées avec Connecteur Raspberry Pi)
- Connecteur Arduino Shield
- 24 E/S FPGA totales
- 6 entrées analogiques asymétriques 0-3,3 V vers XADC
- Connecteur Raspberry Pi
- 28 E/S FPGA totales (8 broches partagées avec Pmod Un port)
- 2 LED RVB Connecteurs d'extension
- Deux ports Pmod standard
- 16 E/S FPGA totales (8 broches partagées avec Connecteur Raspberry Pi)
- Connecteur Arduino Shield
- 24 E/S FPGA totales
- 6 entrées analogiques asymétriques 0-3,3 V vers XADC
- Connecteur Raspberry Pi
- 28 E/S FPGA totales (8 broches partagées avec Pmod Un port)

## 3- Pmod interface : Peripheral Module interface

 <img alt="numerique" src="https://github.com/madou-sow/FPGA-PYNQ-Z2-langage-VHDL/blob/main/images/figurePynqZ2.png" width=70% height=70%  title="numerique"/>
 
## 4- Superposition de base (Base Overlay)

Le but de la conception de la superposition de base est de permettre à PYNQ d'utiliser des
périphériques sur une carte prête à l'emploi. La conception inclut une adresse IP matérielle pour
contrôler les périphériques sur la carte cible et connecte ces blocs IP au Zynq PS. Si une
superposition de base est disponible pour une carte, les périphériques peuvent être utilisés à partir
de l'environnement Python immédiatement après le démarrage du système.
Les périphériques de la carte incluent généralement des périphériques GPIO (voyants,
commutateurs, boutons), vidéo, audio et autres interfaces personnalisées.
Comme la superposition de base inclut IP pour les périphériques sur une carte, elle peut également
être utilisée comme conception de référence pour créer de nouvelles superpositions personnalisées.
Dans le cas des interfaces à usage général, par exemple des en-têtes Pmod ou Arduino, la
superposition de base peut inclure un PYNQ MicroBlaze. Un PYNQ MicroBlaze permet de
contrôler des appareils avec différentes interfaces et protocoles sur le même port sans nécessiter de
modification de la conception de la logique programmable.

 <img alt="numerique" src="https://github.com/madou-sow/FPGA-PYNQ-Z2-langage-VHDL/blob/main/images/schema-PynqZ2.png" width=70% height=70%  title="numerique"/>

## 5- Superposition Logictools (Overlay Logictools)
La superposition logictools se compose de blocs matériels programmables à connecter à des circuits logiques
numériques externes. Des machines à états finis, des fonctions logiques booléennes et des modèles
numériques peuvent être générés à partir de Python. Un commutateur programmable connecte les entrées et
les sorties des blocs matériels aux broches IO externes. La superposition logictools peut également avoir un
analyseur de trace pour capturer les données de l'interface IO à des fins d'analyse et de déboguage.

## 6- Outils logiques PYNQ-Z2
La superposition logictools du PYNQ-Z2 comporte deux instances du LCP (Logic Control Processor)
logictools; l'un connecté à l'en-tête Arduino et l'autre connecté à l'en-tête RPi (Raspberry Pi).
L'en-tête Arduino a 20 broches et le RPi a 26 broches qui peuvent être utilisées comme GPIO pour le LCP.
Les 4 LED et 4 boutons poussoirs peuvent également être connectés à l'un ou l'autre LCP, augmentant ainsi
le nombre d'entrées disponibles. Notez que les voyants et les boutons-poussoirs sont partagés et ne peuvent
être utilisés que par un LCP à la fois.

## 7- Bibliothèques PYNQ

Les systèmes embarqués typiques prennent en charge une combinaison fixe de périphériques (par exemple
SPI, IIC, UART, vidéo, USB). Il peut également y avoir des GPIO (broches d'entrée/sortie à usage général) disponibles. Le nombre de GPIO disponibles dans un système embarqué basé sur le processeur est
généralement limité, et le GPIO est également contrôlé par le processeur principal. En tant que processeur principal qui gère le reste du système, les performances GPIO sont généralement limitées.
Les plates-formes Zynq ont généralement beaucoup plus de broches d'E/S disponibles qu'un système
embarqué classique. Des contrôleurs matériels dédiés et des processeurs logiciels supplémentaires peuvent être implémentés dans le PL et connectés à des interfaces externes.

PYNQ fonctionne sous Linux qui utilise par défaut les périphériques Zynq PS suivants: Carte SD pour
démarrer le système et héberger le système de fichiers Linux, Ethernet pour se connecter au notebook
Jupyter, UART pour l'accès au terminal Linux et USB.

Le port USB et d'autres interfaces standard peuvent être utilisés pour connecter des périphériques USB
standard et d'autres périphériques au Zynq PS où ils peuvent être contrôlés à partir de Python/Linux. Comme le PL est programmable, une superposition qui fournit des contrôleurs pour ces périphériques ou interfaces doit être chargée avant de pouvoir être utilisée.

Une bibliothèque d'IP matérielle est incluse dans Vivado et peut être utilisée pour se connecter à un large éventail de normes et de protocoles d'interface. PYNQ fournit une API Python pour un certain nombre de périphériques courants, notamment la vidéo (entrée et sortie HDMI), les périphériques GPIO (boutons, commutateurs, LED) et les capteurs et actionneurs. L'API PYNQ peut également être étendue pour prendre en charge des adresses IP supplémentaires.
Les plates-formes Zynq ont généralement un ou plusieurs en-têtes ou interfaces qui permettent de connecter des périphériques externes, ou de se connecter directement aux broches Zynq PL. Notez que si un
périphérique peut être physiquement connecté aux broches Zynq PL, un contrôleur doit être intégré à la
superposition et un pilote logiciel fourni avant que le périphérique puisse être utilisé.
Les bibliothèques PYNQ prennent en charge le sous-système PynqMicroBlaze, permettant le chargement des
applications précompilées et la création et la compilation de nouvelles applications à partir de Jupyter.

PYNQ prend également en charge le contrôle de bas niveau d'une superposition, y compris la lecture/écriture
d'E/S mappées en mémoire, l'allocation de mémoire (par exemple, pour une utilisation par un maître PL), le
contrôle et la gestion d'une superposition (téléchargement d'une superposition, lecture d'IP dans une
superposition ), et contrôle de bas niveau du PL (téléchargement d'un train binaire).
