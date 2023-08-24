#! /usr/bin/python3
# -*- coding: utf-8 -*-

import subprocess
import tkinter as tk
"""
def Win_crea():
    subprocess.call("./win_crea.py", shell=True)

def Win_supp():
    subprocess.call("./win_supp.py", shell=True)

def Util_AD():
    subprocess.call("./win_util_ad.py", shell=True)

def Win_backup():
    subprocess.call("./win_z_backup.py", shell=True)
"""
def Lin_crea():
    subprocess.call("./lin_crea.py", shell=True)

def Lin_supp():
    subprocess.call("./lin_supp.py", shell=True)

def Util_lin():
    subprocess.call("./lin_util.py", shell=True)

def Lin_backup():
    subprocess.call("./lin_z_backup.py", shell=True)

# Création de la fenêtre principale
fenetre = tk.Tk()

# Création de la barre de menus
barre_menus = tk.Menu(fenetre)
fenetre.config(menu=barre_menus)
"""
# Menu Windows
menu_windows = tk.Menu(barre_menus, tearoff=False)
barre_menus.add_cascade(label="Windows", menu=menu_windows)
menu_windows.add_command(label="Creation utilisateur", command=Win_crea)
menu_windows.add_command(label="Suppression utilisateur", command=Win_supp)
menu_windows.add_command(label="Liste des utilisateurs dans l'AD", command=Util_AD)
menu_windows.add_command(label="Sauvegarde données utilisateur", command=Win_backup)
"""

# Menu Linux
menu_linux = tk.Menu(barre_menus, tearoff=False)
barre_menus.add_cascade(label="Linux", menu=menu_linux)
menu_linux.add_command(label="Creation utilisateur", command=Lin_crea)
menu_linux.add_command(label="Suppression utilisateur", command=Lin_supp)
menu_linux.add_command(label="Liste des utilisateurs dans linux", command=Util_lin)
menu_linux.add_command(label="Sauvegarde données utilisateur", command=Lin_backup)

# Menu Quitter
menu_quitter = tk.Menu(barre_menus, tearoff=False)
barre_menus.add_cascade(label="Quitter", menu=menu_quitter)
menu_quitter.add_command(label='Quitter', command=fenetre.destroy)

# Lancement de la boucle principale
fenetre.mainloop()
