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

### 17 - Présentation KMeans.py sans aucune implémentation du FPGA

```
#!/usr/bin/python
#
# Source: http://rosettacode.org/wiki/K-means%2B%2B_clustering#Python
#
from math import pi, sin, cos
from collections import namedtuple
from random import random, choice
from copy import copy
try:
#import psyco
#psyco.full()
#psyco is no more maintened => pypy
import pypy
except ImportError:
pass
import time
from functools import wraps
PROF_DATA = {}
def profile(fn):
  @wraps(fn)
  def with_profiling(*args, **kwargs):
        start_time = time.time()
        ret = fn(*args, **kwargs)
        elapsed_time = time.time() - start_time
        if fn.__name__ not in PROF_DATA:
        PROF_DATA[fn.__name__] = [0, []]
        PROF_DATA[fn.__name__][0] += 1
        PROF_DATA[fn.__name__][1].append(elapsed_time)
        return ret
        return with_profiling

def print_prof_data():
      for fname, data in PROF_DATA.items():
      max_time = max(data[1])
      avg_time = sum(data[1])/len(data[1])
      print ("Function %s called %d times.\n" % (fname, data[0]))
      print ('Execution time max: %.10f, average: %.10f' % (max_time,
      avg_time))
def clear_prof_data():
      global PROF_DATA
      PROF_DATA = {}
FLOAT_MAX = 1e100
class Point:
__slots__ = ["x", "y", "group"]

      def __init__(self, x=0.0, y=0.0, group=0):
      self.x, self.y, self.group = x, y, group
@profile
def generate_points(npoints, radius):
      points = [Point() for _ in range(npoints)]
      # note: this is not a uniform 2-d distribution
      for p in points:
          r = random() * radius
          ang = random() * 2 * pi
          p.x = r * cos(ang)
          p.y = r * sin(ang)
          return points
@profile
def nearest_cluster_center(point, cluster_centers):
"""Distance and index of the closest cluster center"""
        @profile
        def sqr_distance_2D(a, b):
        return (a.x - b.x) ** 2
        +
        (a.y - b.y) ** 2
        min_index = point.group
        min_dist = FLOAT_MAX
        for i, cc in enumerate(cluster_centers):
        d = sqr_distance_2D(cc, point)
        if min_dist > d:
        min_dist = d
        min_index = i
        return (min_index, min_dist)

@profile
def kpp(points, cluster_centers):
      cluster_centers[0] = copy(choice(points))
      d = [0.0 for _ in range(len(points))]

      for i in range(1, len(cluster_centers)):
          sum = 0
          for j, p in enumerate(points):
              d[j] = nearest_cluster_center(p, cluster_centers[:i])[1]
              sum += d[j]
      sum *= random()

      for j, di in enumerate(d):
            sum -= di
            if sum > 0:
                    continue
                    cluster_centers[i] = copy(points[j])
            break
      for p in points:
              p.group = nearest_cluster_center(p, cluster_centers)[0]
@profile
def lloyd(points, nclusters):

cluster_centers = [Point() for _ in range(nclusters)]
# call k++ init
kpp(points, cluster_centers)
lenpts10 = len(points) >> 10
changed = 0
while True:
      # group element for centroids are used as counters
      for cc in cluster_centers:
            cc.x = 0
            cc.y = 0
            cc.group = 0

      for p in points:
            cluster_centers[p.group].group += 1
            cluster_centers[p.group].x += p.x
            cluster_centers[p.group].y += p.y
      ##Modification SOW rajouter except ZeroDivisionError
      #for cc in cluster_centers:
      #       cc.x /= cc.group
      #       cc.y /= cc.group
      for cc in cluster_centers:
            try:
                  cc.x /= cc.group
                  cc.y /= cc.group
            except ZeroDivisionError:
                  cc.group = 0

      # find closest centroid of each PointPtr
      changed = 0
      for p in points:
            min_i = nearest_cluster_center(p, cluster_centers)[0]
            if min_i != p.group:
                  changed += 1
                  p.group = min_i
      # stop when 99.9% of points are good
      if changed <= lenpts10:
            break
      
      for i, cc in enumerate(cluster_centers):
            cc.group = i
      return cluster_centers

def print_eps(points, cluster_centers, W=400, H=400):
      Color = namedtuple("Color", "r g b");
      colors = []
      for i in range(len(cluster_centers)):
          colors.append(Color((3 * (i + 1) % 11)/11.0, (7 * i % 11)/11.0,(9 * i % 11)/11.0))
      max_x = max_y = -FLOAT_MAX
      min_x = min_y = FLOAT_MAX

for p in points:
      if max_x < p.x: max_x = p.x
      if min_x > p.x: min_x = p.x
      if max_y < p.y: max_y = p.y
      if min_y > p.y: min_y = p.y
scale = min(W/(max_x - min_x),
H/(max_y - min_y))
cx = (max_x + min_x)/2
cy = (max_y + min_y)/2

#print "%%!PS-Adobe-3.0\n%%%%BoundingBox: -5 -5 %d %d" % (W + 10, H + 10)

print ("%!PS-Adobe-3.0 EPSF-3.0")
print ("%%Creator: someone or something")
print ("%%%%BoundingBox: 0 0 %d %d" % (W + 1, H + 1))
print ("%%LanguageLevel: 2")
print ("%%Pages: 1")
print ("%%DocumentData: Clean7Bit")

print ("/l {rlineto} def /m {rmoveto} def\n" +
      "/c { .25 sub exch .25 sub exch .5 0 360 arc fill } def\n" +
      "/s { moveto -2 0 m 2 2 l 2 -2 l -2 -2 l closepath " +
      "
      gsave 1 setgray fill grestore gsave 3 setlinewidth" +
      " 1 setgray stroke grestore 0 setgray stroke }def")

for i, cc in enumerate(cluster_centers):
      print ("%g %g %g setrgbcolor" %
              (colors[i].r, colors[i].g, colors[i].b))
      for p in points:
            if p.group != i:
                  continue
            print ("%.3f %.3f c" % ((p.x - cx) * scale + W/2, (p.y - cy) * scale + H/2))
      print ("\n0 setgray %g %g s" % ((cc.x - cx) * scale + W/2, (cc.y - cy) * scale + H/2))
print ("\n%%%%EOF")

if __name__ == '__main__':
        #import re
        import sys
        def usage():
              print("usage: python %s k n" % sys.argv[0])
              print("
              k = number of clusters")
              print("
              n = input size")
              print("
              Without parameters: k=7 n=30000")
              sys.exit(1)
        #print(sys.argv)
        
        if len(sys.argv) == 1:
              npoints = 3000 # default number of points
              k = 3 # default number of clusters
        else:
              if len(sys.argv) < 3:
        usage()
        try:
              k = int(sys.argv[1])
        except ValueError():
              usage()
        try:
              npoints = int(sys.argv[2])
        except ValueError():
              usage()
points = generate_points(npoints, 10)
cluster_centers = lloyd(points, k)
#print_eps(points, cluster_centers)
print_prof_data()

```
