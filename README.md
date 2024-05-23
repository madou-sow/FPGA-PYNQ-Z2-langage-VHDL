## REPRÉSENTATION COMPORTEMENTALE DES SYSTÈMES NUMÉRIQUES

Dans le domaine des systèmes numériques, il existe deux grands domaines d’applications :
- les processeurs (et dérivés : microcontrôleurs, DSP...) qui font du traitement séquentiel
- les systèmes logiques qui font du traitement parallèle

  image

### Synthèse structurelle et description comportementale
Il existe deux moyens pour synthétiser un système numérique logique.
Le premier fait appel aux techniques de synthèse classique ou encore appelée synthèse structurelle. A partir
d’une table de vérité, on obtient les équations logiques des sorties, à partir des entrées, faisant intervenir des
opérateurs logiques .
Cette méthode permet d’obtenir la structure finale du système à concevoir. Chaque opérateur élémentaire
possède sa solution technologique sous forme de circuit intégré (circuits CMOS : 4001/porte XOR,
4081/porte ET, ...). Une fois la carte électronique réalisée, il n’est alors plus possible de modifier la fonction
réalisée.
Une autre méthode consiste à utiliser un composant logique programmable, laissant ainsi la possibilité de
modifier la fonction réalisée à souhait (mise à jour, correction de bugs...).
Il n’est alors plus nécessaire de connaître la structure que devra avoir le système final, mais de pouvoir
simplement son comportement. On parle alors de description comportementale du système. Ceci nécessite
l’utilisation de langage de description de haut niveau, tel que le VHDL ou le Verilog.

### Composants programmables
Il existe trois grandes catégories de systèmes logiques programmables :

- les CPLD (Complex Programmable Logic Device)
- les FPGA (Field Programmable Gate Array)
- les ASIC (Application Specific Integrated Circuit)
