## Synthèse et implémentation du projet
## 31- Description

La synthèse d’un circuit consiste à traduire sa description en blocs disponibles dans la technologie
utilisée. Par exemple, pour un circuit décrit avec un schéma et qui doit être réalisé sur un FPGA,
le processus de synthèse convertit et regroupe les portes logiques du schéma en composantes
réalisables sur le FPGA choisi. Pour un circuit décrit en VHDL, la synthèse analyse le code et infère
des composantes logiques correspondantes à son comportement.
L’implémentation du circuit est divisée en quatre sous étapes :

• la transformation (mapping) : regrouper les composantes obtenues lors de la synthèse dans des
blocs spécifiques du FPGA ;

• la disposition (placement) : choisir des endroits spécifiques sur le FPGA où disposer les blocs
utilisés, et choisir les pattes du FPGA correspondant aux ports d’entrée et de sortie ;

• le routage (routing) : établir des connexions électriques entre les blocs utilisés ; et,

• la configuration (configuration) : convertir toute cette information en un fichier pouvant être
téléchargé sur le FPGA pour le programmer.

## 32- Ports d'entrée et de sortie 

Pendant l’étape de disposition de l’implémentation, il faut assigner des pattes spécifiques du
FPGA à des ports d’entrée et de sortie de son design. Pour le design présent, les ports d’entrée
sont X, Y et Cin, et les ports de sortie sont Cout et S.
L’assignation des ports se fait par l’entremise d’un fichier de contraintes avec l’extension « .xdc»
(pour xilinx design constraints file). 

Ouvrez un éditeur de texte (comme Notepad++) et copiez-y les lignes suivantes. On suppose que
vous utilisez la planchette PYNQ-Z2 du fichier pynq-z2_c.xdc.

```
## LEDs
set_property -dict {PACKAGE_PIN R14 IOSTANDARD LVCMOS33} [get_ports { Cout }]
set_property -dict {PACKAGE_PIN P14 IOSTANDARD LVCMOS33} [get_ports { S }]
## Commutateurs
set_property -dict {PACKAGE_PIN N16 IOSTANDARD LVCMOS33} [get_ports { X }]
set_property -dict {PACKAGE_PIN M14 IOSTANDARD LVCMOS33} [get_ports { Y}]
set_property -dict {PACKAGE_PIN T14 IOSTANDARD LVCMOS33} [get_ports { Cin }]
```



