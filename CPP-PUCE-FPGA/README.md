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
