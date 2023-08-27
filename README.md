Projet 6 - AIC Openclassrooms

Automatiser la gestion utilisateur et la sauvegarde de dossiers Linux

Ce script Python à été créé afin d'effectuer des sauvegardes de manières automatisé et simple, il permet aussi la gestion des utilisateurs.

Un fenetrage tkinter(a_menu.py) permet d'avoir un menu des différents scripts.

Créé par : Anthony Clouye

Date de création : 27/08/2023

Testé avec : Python 3

Ce programme/scripts sont sous Licence Publique Générale GNU V3

Fonctionnement du script

Mettre les différents script sous un même dossier. Lancez le script a_menu.py en tout premier. Il vous affichera la fenetre de gestion des différents scripts d'automatisation.

Ces différents scripts ont été écrit pour un réseau constitué d'une machine Linux ubuntu 18.04 desktop gérant deux réseaux en 192.168.0.0/24 (linux) et 192.168.1.0/24 (windows)

Un menu tkinter se lancant sur la machine linux ubuntu 18.04 desktop vous permet de lancer les différents scripts d'automatisation, il se trouve sur projet6.py. Il contient différents menus :

. Reseau
. Windows_users
. Linux_users
. Sauvegarde
. Quitter
. A propos

Le menu Reseau, contient à ce jour un script Nmap pour deux sous réseau (un reseau linux, un reseau windows)
