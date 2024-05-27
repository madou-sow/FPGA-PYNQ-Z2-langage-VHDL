## COMPILER UN PROGRAMME C++ SUR UN CIRCUIT FPGA
### 1- Lancer Vivado HLS et créer un projet IP (Intellectual Properties) avec le langage C++
L'IP développée est un programme nommé somadd.cpp qui calcule la somme de 2 entiers avec un circuit
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
