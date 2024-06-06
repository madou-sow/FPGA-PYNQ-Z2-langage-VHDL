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

On peut noter que chaque port est identifié dans le fichier, exactement comme il apparaît dans
le code VHDL. Le symbole du dièse (#) indique que le reste de la ligne est un commentaire pour
les fichiers .xdc. Sauvegardez le fichier dans le même répertoire que les autres fichiers sources de
votre design, sous le nom de pynq-z2_c.xdc. Puis, dans Project Manager, faites un clic droit sur
constraints, cliquez sur Add Sources... comme le montre la figure suivante :


 <img alt="numerique" src="https://github.com/madou-sow/FPGA-PYNQ-Z2-langage-VHDL/blob/main/images/contraint-xdc.png" width=70% height=70%  title="numerique"/>


 <img alt="xdc" src="https://github.com/madou-sow/FPGA-PYNQ-Z2-langage-VHDL/blob/main/images/fichier-pynqZ2-xdc.png" width=70% height=70%  title="xdc"/>

**Procédure**

Il vous est maintenant possible de faire la synthèse de votre circuit en vue d’une implémentation
sur le FPGA. Pour ce faire, il faudra utiliser l’onglet Flow Navigator de Vivado (Colonne à gauche):



<img alt="Flow" src="https://github.com/madou-sow/FPGA-PYNQ-Z2-langage-VHDL/blob/main/images/FlowNavigator.png" width=30% height=30%  title="Flow"/>

Pour les opérations de **Synthesis, Implementation et Generate Bitstream**, il faut faire un clique-droit sur Run Synthesis, Run Implementation et Generate Bitstream, respectivement.

**Run Synthesis** : permet de faire la synthèse du circuit en blocs configurables du FPGA.
Run Implementation : permet de faire les mapping et routage nécessaires pour placer le tout sur
le composant FPGA.

**Generate Bitstream** : génère le fichier (.bit) utilisé pour programmer le FPGA.
File > Export > Export Bitstream File full_add_behavioral_add3bits_pynqZ2bit



<img alt="bitstream" src="https://github.com/madou-sow/FPGA-PYNQ-Z2-langage-VHDL/blob/main/images/bitstream-add3bits.png" width=70% height=70%  title="Bits"/>

<img alt="bitstream" src="https://github.com/madou-sow/FPGA-PYNQ-Z2-langage-VHDL/blob/main/images/export-bitsream.png" width=70% height=70%  title="Bits"/>

**Programmation du FPGA et vérification** : Générer le flux binaire et vérifier la fonctionnalité

Une fois les trois étapes (synthèse, implémentation et génération du bitstream) finies, on peut
procéder à la programmation du FPGA.

- Branchez la carte à votre PC, et allumez votre carte (interrupteur à côté du câble mini
USB)  
- Dans la rubrique Program and Debug, cliquez sur Generate Bitstream    
- Après quelques secondes, une fenêtre apparaît, sélectionnez Open Hardware Manager, puis OK
- Cliquez droit sur la cible (xc7z020clg400-1), puis Program Device  

Dans Flow Navigator, cliquez sur Open Hardware Manager => Open Target => Program pour
programmer le FPGA tel que le montrent les figures suivantes :  

Sélectionnez l'appareil et vérifiez que add3bits.bit est sélectionné comme fichier de programmation dans le Cliquez sur le lien Program device> xc7z020clg400-1 dans la barre d'informations verte programmer le périphérique FPGA cible.  
Il existe une autre façon est de faire un clic droit sur l'appareil et de sélectionner Programmer le périphérique


<img alt="tistream" src="https://github.com/madou-sow/FPGA-PYNQ-Z2-langage-VHDL/blob/main/images/Fichier programmebtistream.png" width=70% height=70%  title="tistream"/>


<img alt="Z2" src="https://github.com/madou-sow/FPGA-PYNQ-Z2-langage-VHDL/blob/main/images/ouvertureSessionforPynqZ2.png" width=70% height=70%  title="Z2"/>



<img alt="bitstream" src="https://github.com/madou-sow/FPGA-PYNQ-Z2-langage-VHDL/blob/main/images/ouvertureSessionHardWarePynqZ2.png" width=70% height=70%  title="bitstream"/>

<img alt="bitstream2" src="https://github.com/madou-sow/FPGA-PYNQ-Z2-langage-VHDL/blob/main/images/pynqZ2bitstream2.png" width=70% height=70%  title="bitstream2"/>


