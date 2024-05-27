## COMPILER UN PROGRAMME C++ SUR UN CIRCUIT FPGA
### 1- Lancer Vivado HLS et créer un projet IP (Intellectual Properties) avec le langage C++
L'IP développée est un programme nommé somadd.cpp qui calcule la somme *somadd.cpp* de 2 entiers avec un circuit
FPGA (xc7z020clg400-1)

- Famille du Composant : Zynq 7000  
- Circuit : Pynq-Z2  
- Puce : xc7z020clg400-1

  
```
#include <stdio.h>
#include <math.h>
void somadd (int a, int b, int& c){
#pragma HLS INTERFACE ap_ctrl_none port=return
#pragma HLS INTERFACE s_axilite port=a
#pragma HLS INTERFACE s_axilite port=b
#pragma HLS INTERFACE s_axilite port=c
      c = a + b;
}
```
Vivado HLS utilise des directives de compilation commençant par "**#pragma HLS**" pour que le matériel
interprète le code C/C++.
La première ligne avec prama permet d'initialiser le noyau dès que les données du flux d'entrée sont
disponibles.


 <img alt="hls" src="https://github.com/madou-sow/FPGA-PYNQ-Z2-langage-VHDL/blob/main/images/hls-somadd.png" width=50% height=50%  title="hls"/>

### 2- La Synthèse du Programme s'exécute avec le triangle vert (Run C Synthesis) sur la barre des outils

 <img alt="rsync" src="https://github.com/madou-sow/FPGA-PYNQ-Z2-langage-VHDL/blob/main/images/runcsynthesissomadd.png" width=50% height=50%  title="rsync"/>

### 3- L'exportation en RTL (Register Transfer Level) en format IP et VHDL

<img alt="hls" src="https://github.com/madou-sow/FPGA-PYNQ-Z2-langage-VHDL/blob/main/images/exportRTLasIPexecutution.png" width=50% height=50%  title="hls"/>

 <img alt="rtl" src="https://github.com/madou-sow/FPGA-PYNQ-Z2-langage-VHDL/blob/main/images/exportRTLresultat.png" width=50% height=50%  title="rtl"/>

### 4- Le code source *xsomadd_hw.h (../solution1/impl/ip/drivers/somadd_v1_0/src/)* du driver généré par Vivado HLS indique les adresses pour définir les attributs de la fonction somadd.cpp. Les entrées sont accessibles à travers les adresses *0x10, 0x18* et la sortie à travers l'adresse *0x20*

 <img alt="hwh" src="https://github.com/madou-sow/FPGA-PYNQ-Z2-langage-VHDL/blob/main/images/xsomadd_hwh.png" width=50% height=50%  title="hwh"/>

 ### 5- Lancer Vivado IP integrator et importer l'IP créée depuis le dépôt IP

  <img alt="imp" src="https://github.com/madou-sow/FPGA-PYNQ-Z2-langage-VHDL/blob/main/images/Importation-IP-Crée.png" width=50% height=50%  title="imp"/>

### 6- Créer un bloc design, ajouter l'IP somadd créée, connecter automatiquement de l'IP au processing system Pynq-Z2 et créer le design


  <img alt="imp" src="https://github.com/madou-sow/FPGA-PYNQ-Z2-langage-VHDL/blob/main/images/diagramVivadoIP.png" width=50% height=50%  title="imp"/>

### 7- Exporter les 2 fichiers (.tcl et .bit) avec les même préfixes "Fichier/Export/ à par de Vivado IP

- Export Block Design : lipn.tcl  
- Export Bitstream File : lipn.bit  

### 8- Créer le fichier lipn.hwh en copiant le fichier "/tempo/xilinx-vivado/project-vivado-hls/mamadou/xc7z020clg400-1/ipsomadd/ipsomadd.srcs/sources_1/bd/design_1/hw_handoff/

design_1.hwh" en lui donnant le même préfixe que les fichiers .tcl et .bit


  <img alt="lipnhwh" src="https://github.com/madou-sow/FPGA-PYNQ-Z2-langage-VHDL/blob/main/images/fichier-lipnhwh.png" width=70% height=70%  title="lipnhwh"/>

### 9- Mise en place de la carte FPGA PYNQ-Z2

- Alimenter électriquement la carte avec le câble USB  
- placer sur le réseau local votre carte FPGA à l'aide d'une adresse IP statique et un câble ethernet  
- à l'aide du navigateur chrome accéder aux notebookjupyter "http://10.10.1.72:9090/" avec les idenfiants xilinx et xilinx  
- importer les 3 fichiers lipn.tcl, lipn.bit et lipn.hwh

    <img alt="liste3" src="https://github.com/madou-sow/FPGA-PYNQ-Z2-langage-VHDL/blob/main/images/liste3fichiersexportes.png" width=70% height=70%  title="liste3"/>

### 10- Charger le fichier Bitstream lipn.bit contenant le overlay et vérifier si le module IP Blocks est effectivement chargé

  <img alt="jupyter1" src="https://github.com/madou-sow/FPGA-PYNQ-Z2-langage-VHDL/blob/main/images/jupyter1.png" width=80% height=80%  title="jupyter1"/>

### 11- Test de vérification du design
 
 <img alt="jupyter2" src="https://github.com/madou-sow/FPGA-PYNQ-Z2-langage-VHDL/blob/main/images/jupyter2.png" width=80% height=80%  title="jupyter2"/>

 ### 12- Programme overlay-somadd.y

Implémentation de notre code sur le FPGA de la carte PYNQ-Z2, à travers python via l'environnement
Jupyter NoteBook avec des entrées (2,5)
 
 <img alt="jupyter5" src="https://github.com/madou-sow/FPGA-PYNQ-Z2-langage-VHDL/blob/main/images/jupyter5.png" width=80% height=80%  title="jupyter5"/>

### 13- Test du Programme overlay-somadd.y dans un terminal avec lipn.hwh

 <img alt="jupyter4" src="https://github.com/madou-sow/FPGA-PYNQ-Z2-langage-VHDL/blob/main/images/jupyter4.png" width=80% height=80%  title="jupyter4"/>

 
### 14- Test du Programme overlay-somadd.y sans la présence de lipn.hwh

 <img alt="overlay jupyter" src="https://github.com/madou-sow/FPGA-PYNQ-Z2-langage-VHDL/blob/main/images/overlay-jupyter-sans-h.png" width=80% height=80%  title="overlay jupyter"/>

### 15- Rajoutons notre design version 1 à l'algorithme KMeans : l'implémentation de la fonction som_add_2D sur FPGA

 <img alt="design kmeans" src="https://github.com/madou-sow/FPGA-PYNQ-Z2-langage-VHDL/blob/main/images/notredesign-dans-KMeans.png" width=80% height=80%  title="design kmeans"/>

### 16- Rajoutons notre design version 2 à l'algorithme KMeans : l'implémentation de la fonction som_add_2D sur FPGA

 <img alt="v2 design kmeans" src="https://github.com/madou-sow/FPGA-PYNQ-Z2-langage-VHDL/blob/main/images/v2design-overlay-somadd.png" width=80% height=80%  title="v2 design kmeans"/>
