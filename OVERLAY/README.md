# OVERLAYS PYNQ

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

## 8- Méthodologie de conception de superposition

Comme décrit dans l'introduction de PYNQ, les superpositions sont analogues aux bibliothèques de logiciels.
Un programmeur peut télécharger des superpositions dans le Zynq® PL au moment de l'exécution pour
fournir les fonctionnalités requises par l'application logicielle.

Une superposition est une classe de conception de logique programmable. Les conceptions de logique
programmable sont généralement hautement optimisées pour une tâche spécifique. Cependant, les
superpositions sont conçues pour être configurables et réutilisables pour un large éventail d'applications. Une
superposition PYNQ aura une interface Python, permettant à un programmeur logiciel de l'utiliser comme
n'importe quel autre package Python.

Un programmeur de logiciel peut utiliser une superposition, mais ne créera généralement pas de
superposition, car cela nécessite généralement un haut degré d'expertise en conception matérielle.

Un certain nombre de composants sont nécessaires pour créer une superposition:
- Paramètres de la carte
- Interface PS-PL
- Processeurs MicroBlaze Soft
- Intégration Python/C
- Python AsyncIO
- API de superposition Python
- Emballage Python

## 9- Conception de superposition

Une superposition se compose de deux parties principales; la conception PL (bitstream) et le fichier Tcl du
schéma de principe du projet. La conception de superposition est une tâche spécialisée pour les ingénieurs en
matériel. Cette section suppose que le lecteur a une certaine expérience de la conception numérique, de la
construction de systèmes Zynq et des outils de conception Vivado.

**Conception PL**

Le logiciel Xilinx® Vivado est utilisé pour créer un design Zynq. Un fichier bitstream ou binaire (fichier .bit)
sera généré et pourra être utilisé pour programmer le Zynq PL.

Le concepteur de matériel est encouragé à prendre en charge la programmabilité dans l'adresse IP utilisée
dans une superposition PYNQ. Une fois l'IP créée, la conception PL est réalisée de la même manière que
toute autre conception Zynq. IP dans une superposition qui peut être contrôlée par PYNQ sera mappée en
mémoire, connectée à GPIO. IP peut également avoir une connexion principale au PL. PYNQ fournit des
bibliothèques Python pour s'interfacer avec la conception PL et qui peuvent être utilisées pour créer leurs
propres pilotes. L'API Python pour une superposition sera et sera couverte dans les sections suivantes.
Superposer le fichier Tcl.
Le Tcl de la conception de bloc Vivado IP Integrator pour la conception PL est utilisé par PYNQ pour identifier automatiquement la configuration du système Zynq, IP, y compris les versions, les interruptions, les réinitialisations et autres signaux de contrôle. Sur la base de ces informations, certaines parties de la
configuration du système peuvent être modifiées automatiquement à partir de PYNQ, les pilotes peuvent être
automatiquement attribués, les fonctionnalités peuvent être activées ou désactivées et les signaux peuvent
être connectés aux méthodes Python correspondantes.
Le fichier Tcl doit être généré et fourni avec le fichier bitstream dans le cadre d'une superposition. Le fichier
Tcl peut être généré dans Vivado en exportant le schéma de principe IP Integrator à la fin du processus de
conception de superposition. Le fichier Tcl doit être fourni avec un flux binaire lors du téléchargement d'une
superposition. La classe PYNQ PL analysera automatiquement le Tcl.
Un fichier Tcl personnalisé ou créé manuellement peut être utilisé pour créer un projet Vivado, mais Vivado
doit être utilisé pour générer et exporter le fichier Tcl pour le diagramme. Ce Tcl généré automatiquement
doit garantir qu'il peut être analysé correctement par le PYNQ.
10- Programmabilité
Une superposition doit avoir une programmabilité post-bitstream pour permettre la personnalisation du
système. Un certain nombre de blocs IP PYNQ réutilisables sont disponibles pour prendre en charge la
programmabilité. Par exemple, un PYNQ MicroBlaze peut être utilisé sur les interfaces Pmod et Arduino.
L'adresse IP des différentes superpositions peut être réutilisée pour fournir une configurabilité au moment de
l'exécution.

## 11- Paramètres Zynq PS

Un projet Vivado pour une conception Zynq se compose de deux parties; la conception PL et les paramètres
de configuration PS.
L'image PYNQ utilisée pour démarrer la carte configure le Zynq PS au moment du démarrage. Cela
corrigera la plupart de la configuration PS, y compris la configuration de la DRAM et l'activation des
périphériques Zynq PS, y compris la carte SD, Ethernet, USB et UART qui sont utilisés par PYNQ.
La configuration PS comprend également les paramètres des horloges système, y compris les horloges
utilisées dans le PL. Les horloges PL peuvent être programmées au moment de l'exécution pour correspondre
aux exigences de la superposition. Ceci est géré automatiquement par la classe PYNQ Overlay
Pendant le processus de téléchargement d’une nouvelle superposition, la configuration de l’horloge sera
analysée à partir du fichier Tcl de la superposition. Les nouveaux paramètres d'horloge de la superposition
seront appliqués automatiquement avant le téléchargement de la superposition.

## 12- Interfaces PS/PL

Le Zynq dispose de 9 interfaces AXI entre le PS et le PL. Du côté PL, il y a 4x ports AXI Master HP (High
Performance), 2x ports AXI GP (General Purpose), 2x ports AXI Slave GP et 1x AXI Master ACP port. Il
existe également des contrôleurs GPIO dans le PS qui sont connectés au PL.

Il existe quatre classes pynq qui sont utilisées pour gérer le mouvement des données entre les interfaces Zynq
PS (y compris la PS DRAM) et PL.

GPIO - Entrée/sortie à usage général  
MMIO - E/S mappées en mémoire  
Xlnk - Allocation de mémoire  
DMA - Accès direct à la mémoire  

La classe utilisée dépend de l'interface Zynq PS à laquelle l'IP est connecté et de l'interface de l'IP.
Le code Python exécuté sur PYNQ peut accéder à une adresse IP connectée à un esclave AXI connecté à un
port GP. MMIO peut être utilisé pour ce faire.

L'IP connecté à un port maître AXI n'est pas sous le contrôle direct du PS. Le port maître AXI permet à l'IP
d'accéder directement à la DRAM. Avant de faire cela, la mémoire doit être allouée à l'adresse IP à utiliser.
La classe Xilink peut être utilisée pour cela. Pour un transfert de données plus performant entre PS DRAM et
un IP, des DMA peuvent être utilisés. PYNQ fournit une classe DMA.

Lors de la conception de votre propre superposition, vous devez tenir compte du type d'IP dont vous avez
besoin et de la manière dont elle se connectera au PS. Vous devriez alors être en mesure de déterminer les
classes dont vous avez besoin pour utiliser l'adresse IP.
