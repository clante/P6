Projet 6 - AIC Openclassrooms

Automatiser la gestion utilisateur et la sauvegarde de dossiers Linux

Ce script Python à été créé afin d'effectuer des sauvegardes de manières automatisé et simple, il permet aussi la gestion des utilisateurs.

Un fenetrage tkinter(a_menu.py) permet d'avoir un menu des différents scripts.

Créé par : Anthony Clouye

Date de création : 27/08/2023

Testé avec : Python 3

Fonctionnement du script

Mettre les différents script sous un même dossier. Lancez le script a_menu.py en tout premier. Il vous affichera la fenetre de gestion des différents scripts d'automatisation.

Ces différents scripts ont été écrit pour un réseau constitué d'une machine Linux ubuntu 22.04 LTS desktop gérant le réseau Linux en 10.0.2.14/24

Un menu tkinter se lancant sur la machine linux ubuntu 22.04 LTS desktop vous permet de lancer les différents scripts d'automatisation, il se trouve sur a_menu.py. Il contient différents menus :

. Linux_users

. Quitter


#Le menu général, contient 2 sous-menu: Linux et Quitter : 

![](https://github.com/clante/p6/blob/master/image/01.png)

<img src="https://github.com/clante/p6/blob/master/image/01.png" width="580"/>

#Le menu linux-users contient : Liste utilisateur linux, Création utilisateur linux, Suppression utilisateur linux :

![image menu linux](https://github.com/clante/p6/blob/master/image/02linux.png)

#Tous ces scripts se lancent via une connexion ssh ou pexpect pxssh : 

![image histo](https://github.com/clante/p6/blob/master//image/histograme.png)

#a_menu.py : lance le menu d'automatisation général

#lin_crea.py : lance le script de création utilisateur linux

#lin_supp.py : lance le script de supression utilisateur linux

#lin_util.py : récupère la liste des utilisateurs linux

#lin_z_backup.py : sauvegarde d'un utilisateur

#Quitter : quitte le programme d'automatisation des taches administrateur.


