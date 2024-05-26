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
