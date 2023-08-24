#! /usr/bin/python3
# -*- coding: utf-8 -*-

from pexpect import pxssh
import tkinter as tk
from tkinter import scrolledtext

# Informations création du compte
nouvel_utilisateur = ''
nouveau_mot_de_passe = ''

# Fenêtre Tkinter
window = tk.Tk()
window.title('Création de compte utilisateur Linux')
window.geometry('500x350')

# Zone de texte pour afficher les résultats
results_text = scrolledtext.ScrolledText(window, width=60, height=10)
results_text.pack(pady=10)

def creer_compte_utilisateur():
    # global nouvel_utilisateur, nouveau_mot_de_passe
    nouvel_utilisateur = username_entry.get()
    nouveau_mot_de_passe = password_entry.get()

    try:
        # connexion à la machine distante
        s = pxssh.pxssh()
        hostname = '10.0.2.14' # attribution variable hostname
        username = 'ac' # attribution variable username
        password = 'Pza123RR' # attribution variable password

        addnu = 'sudo useradd -p ' + str(nouveau_mot_de_passe) + str(' -m ') + str(nouvel_utilisateur)
        mdpnu = 'sudo chage -d0 ' + str(nouvel_utilisateur)
        
        # Commandes pour créer l'utilisateur
        s.login(hostname, username, password)
        s.sendline(addnu) # ajout de l'utilisateur
        s.sendline(password)
        s.sendline(mdpnu) # change mdp 1ière connection
        s.sendline(password)
   
        # Déconnexion
        s.logout()

    except pxssh.ExceptionPxssh as e:
        print("utilisateur non créé :")
        print(nouvel_utilisateur)

# Entrée pour le nom d'utilisateur
username_label = tk.Label(window, text='Nom d\'utilisateur :')
username_label.pack()
username_entry = tk.Entry(window, width=30)
username_entry.pack()

# Entrée pour le mot de passe
password_label = tk.Label(window, text='Mot de passe de 8 caractères minimum :')
password_label.pack()
password_entry = tk.Entry(window, width=30, show='*')
password_entry.pack()

# Bouton pour créer le compte utilisateur
create_button = tk.Button(window, text='Créer le compte utilisateur', command=creer_compte_utilisateur)
create_button.pack(pady=10)

window.mainloop()

#s.sendline('sudo passwd -e ' + str(nouvel_utilisateur)) # change mdp 1ière connection
