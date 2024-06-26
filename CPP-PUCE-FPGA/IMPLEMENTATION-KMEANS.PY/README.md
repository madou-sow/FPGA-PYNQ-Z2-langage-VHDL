### 17 - Présentation *KMeans.py* sans aucune implémentation du FPGA

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
      " gsave 1 setgray fill grestore gsave 3 setlinewidth" +
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
              print(" k = number of clusters")
              print(" n = input size")
              print(" Without parameters: k=7 n=30000")
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

## 18 - Présentation *KMeansWithFPGA-Copy1-somadd-sowV1.py* avec une implémentation version 1 du FPGA

KMeans++ Clustering est une classification de données de sorte que les données d'un même cluster soit
similaire dans un sens. La tâche consiste à implémenter l'algorithme KMeans++ en créant une fonction qui
prend 2 arguments K le nombre de clusters et N le nombre de données à classer. K est un entier positif et
l'ensemble de données N est une liste de points dans un plan cartésien. Il a été rajouter une fonction de
profilage permettant de connaître le comportement à l'exécution de K-Means, des fonctions, les temps passé
dans chacune de d'elles et le nombre d'appel (exprimé en times). Les diverses fonctions dans le programme
KMeans sont generate_point, somadd, nearest_cluster_center, kpp et lloyd. La description des fonctions sont
dans le tableau d'en dessous

| Fonction | Description | 
| --- | --- |
| generate_points | génère un ensemble de points aléatoires| 
| somadd | renvoie la somme de 2 entiers |
| nearest_cluster_center | renvoie la distance et l'indice du centre de cluster le plus proche |
| kpp | initialise les centres des clusters | 
| lloyd | recalcule à chaque itération les centres des clusters et affecte chaque point de nouveau au cluster dont le centre est le plus proche jusqu'à convergence |


```
#!/usr/bin/python
#
# Adaptation: C. Cerin & M. SOW
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
          print ('Execution time max: %.10f, average: %.10f' % (max_time, avg_time))

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

#### RAJOUT Debut
class AddDriver(DefaultIP):
        def __init__(self, description):
            super().__init__(description=description)

        bindto = ['xilinx.com:hls:somadd:1.0']

        def som_add_2D(self, a, b, c, d):
              self.write(0x10, a)
              self.write(0x18, b)
              self.write(0x20, c)
              self.write(0x28, d)
              return self.read(0x30)

ov = Overlay('/home/xilinx/jupyter_notebooks/sow/14juillet/lipn.bit',
download=False)
ov.download()
dist_ip = ov.somadd_0


@profile
def nearest_cluster_center(point, cluster_centers):
"""Distance and index of the closest cluster center"""
        @profile
        def som_add_2D(a, b):
              return dist_ip.som_add_2D(int(a.x), int(a.y),int(b.x),int(b.y))
        min_index = point.group
        min_dist = FLOAT_MAX

        for i, cc in enumerate(cluster_centers):
            d = som_add_2D(cc, point)
            if min_dist > d:
                  min_dist = d
                  min_index = i
        #print(d)
        return (min_index, min_dist)
### RAJOUT Fin

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
scale = min(W/(max_x - min_x),H/(max_y - min_y))
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
      " gsave 1 setgray fill grestore gsave 3 setlinewidth" +
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
              print(" k = number of clusters")
              print(" n = input size")
              print(" Without parameters: k=7 n=30000")
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


## 19 - Présentation *KMeansWithFPGA-Copy1-somadd-sowV2.py* avec une implémentation version 2 du FPGA


```
#!/usr/bin/python
#
# Adaptation: C. Cerin & M. SOW
#

from math import pi, sin, cos
from collections import namedtuple
from random import random, choice
from copy import copy
from pynq import Overlay

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
          print ('Execution time max: %.10f, average: %.10f' % (max_time, avg_time))

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

#### RAJOUT Debut
# class AddDriver(DefaultIP):
#        def __init__(self, description):
#            super().__init__(description=description)
#
#        bindto = ['xilinx.com:hls:somadd:1.0']

#        def som_add_2D(self, a, b, c, d):
#              self.write(0x10, a)
#             self.write(0x18, b)
#              self.write(0x20, c)
#              self.write(0x28, d)
#              return self.read(0x30)

ov = Overlay('/home/xilinx/jupyter_notebooks/sow/14juillet/lipn.bit',
download=False)
ov.download()
dist_ip = ov.somadd_0


@profile
def nearest_cluster_center(point, cluster_centers):
"""Distance and index of the closest cluster center"""

### Modification Debut
        @profile
        def som_add_2D(a, b):
              dist_ip.write(0x10, int(a.x))
              dist_ip.write(0x18, int(a.y))
              dist_ip.write(0x20, int(b.x))
              dist_ip.write(0x28, int(b.y))
              x = dist_ip.read(0x30)
              return x

        min_index = point.group
        min_dist = FLOAT_MAX
### Modification Fin

        for i, cc in enumerate(cluster_centers):
            d = som_add_2D(cc, point)
            if min_dist > d:
                  min_dist = d
                  min_index = i
        #print(d)
        return (min_index, min_dist)
### RAJOUT Fin

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
scale = min(W/(max_x - min_x),H/(max_y - min_y))
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
      " gsave 1 setgray fill grestore gsave 3 setlinewidth" +
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
              print(" k = number of clusters")
              print(" n = input size")
              print(" Without parameters: k=7 n=30000")
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

## 20- Tests et Observations

### 20.1- Kmeans.py avec K=3 clusters

**Temps d'exécution moyen :**  *python3 kmeans.py 3 "N nombre points"*

| Fonction | generate_points | sqr_distance_2D | nearest_cluster_center | kpp | lloyd | |
| --- | --- |  --- |  --- | --- | --- | --- |
| N nombre points = 3000 | - | 0,0383 s | 0,0000128 s | 0,0001588 s | 1,4039 s | 9,77 s |
| Nombre d'appels | 1 time | 153000 times | 54000 times | 1 time | 1 time | |
| N nombre points = 30000 | - | 0,404 s | 0,0000126 s | 0,000155 s | 13,940 s | 74,78 s |
| Nombre d'appels | 1 time | 117000 times | 420000 times | 1 time | 1 time | |

### 20.2- KMeansWithFPGA-Copy1-somadd-sowV1.py avec K=3 clusters

**Temps d'exécution moyen :**  *python3 KMeansWithFPGA-Copy1-somadd-sowV1.py 3 "N nombre points"*

| Fonction | generate_points | som_add_2D | nearest_cluster_center | kpp | lloyd | |
| --- | --- |  --- |  --- | --- | --- | --- |
| N nombre points = 3000 | - | 0,041 s | 0,000186 s | 0,000550 s | 4,726 s | 6,88 s |
| Nombre d'appels | 1 time | 27000 times | 12000 times | 1 time | 1 time | |
| N nombre points = 30000 | - | 0,767 s | 0,000186 s | 0,000552 s | 47,509 s | 69,16 s |
| Nombre d'appels | 1 time | 270000 times | 120000 times | 1 time | 1 time | |

### 20.3 - KMeansWithFPGA-Copy1-somadd-sowV2.py avec K=3 clusters

**Temps d'exécution moyen :**  *python3 kmeansWithFPGA-Copy1-somadd-sowV2.py 3 "N nombre points"*

| Fonction | generate_points | som_add_2D | nearest_cluster_center | kpp | lloyd | |
| --- | --- |  --- |  --- | --- | --- | --- |
| N nombre points = 3000 | - | 0,0394 s | 0,000187 s | 0,000552 s | 4,737 s | 6,92 s |
| Nombre d'appels | 1 time | 27000 times | 12000 times | 1 time | 1 time | |
| N nombre points = 30000 | - | 0,769 s | 0,000195 s | 0,000573 s | 49,10 s | 71,69 s |
| Nombre d'appels | 1 time | 270000 times | 120000 times | 1 time | 1 time | |



 <img alt="RecapTests" src="https://github.com/madou-sow/FPGA-PYNQ-Z2-langage-VHDL/blob/main/images/tableau-recap-tests.png" width=50% height=50%  title="RecapTests"/>
