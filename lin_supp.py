#! /usr/bin/python3
# -*- coding: utf-8 -*-

from pexpect import pxssh
import tkinter as tk
from tkinter import scrolledtext

# Informations création du compte
utilisateur = ''

# Fenêtre Tkinter
window = tk.Tk()
window.title('Suppression du compte utilisateur Linux')
window.geometry('500x350')

# Zone de texte pour afficher les résultats
results_text = scrolledtext.ScrolledText(window, width=60, height=10)
results_text.pack(pady=10)

def supp_compte_utilisateur():
    # global nouvel_utilisateur, nouveau_mot_de_passe
    utilisateur = username_entry.get()
    
    try:
        # connexion à la machine distante
        s = pxssh.pxssh()
        hostname = '10.0.2.14' # attribution variable hostname
        username = 'ac' # attribution variable username
        password = 'Pza123RR' # attribution variable password

        # Commandes pour supprimer l'utilisateur
        s.login(hostname, username, password)
        s.sendline('sudo su')   # passage en admin
        s.sendline(password) # mdp admin
        s.sendline('userdel -r ' + str(utilisateur)) # suppression de l'utilisateur

        # Déconnexion
        s.logout()

    except pxssh.ExceptionPxssh as e:
        print("utilisateur créé.")


# Entrée pour le nom d'utilisateur
username_label = tk.Label(window, text='Nom d\'utilisateur :')
username_label.pack()
username_entry = tk.Entry(window, width=30)
username_entry.pack()

# Bouton pour créer le compte utilisateur
create_button = tk.Button(window, text='Supprimer le compte utilisateur', command=supp_compte_utilisateur)
create_button.pack(pady=10)

window.mainloop()
