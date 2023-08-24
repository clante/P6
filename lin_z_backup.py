#! /usr/bin/python3
# -*- coding: utf-8 -*-

from pexpect import pxssh
import tkinter as tk
from tkinter import scrolledtext

# Informations création du compte
n_user = ''

# Fenêtre Tkinter
window = tk.Tk()
window.title('Sauvegarde de compte utilisateur Linux')
window.geometry('500x300')

# Zone de texte pour afficher les résultats
results_text = scrolledtext.ScrolledText(window, width=60, height=10)
results_text.pack(pady=10)

def sauvegarder_compte_utilisateur():
    # global nouvel_utilisateur, nouveau_mot_de_passe
    n_user = username_entry.get()
    
    try:
        # connexion à la machine distante
        s = pxssh.pxssh()
        hostname = '10.0.2.14' # attribution variable hostname
        username = 'ac' # attribution variable username
        password = 'Pza123RR' # attribution variable password

        # Commandes pour sauvegarder l'utilisateur
        s.login(hostname, username, password)
        s.sendline('ls')
        s.sendline('tar -czvf ' + str(n_user) + '_bk.tar.gz /home/ac') # comp de l'utilisateur
        #s.sendline('scp ' + str(n_user) + '_bk.tar.gz p6@10.0.2.10:~/Bureau/backup ') # sauvegarde
        #s.sendline('rm ' +str(n_user) + '_bk.tar.gz') # supp fichier du poste

        #print('scp ' + str(n_user) + '_bk.tar.gz p6@10.0.2.10:~/Bureau/backup')
   
        # Déconnexion
        s.logout()
        print("utilisateur sauvegardé.")

    except pxssh.ExceptionPxssh as e:
        print("utilisateur non sauvegardé :")
        print(n_user)

# Entrée pour le nom d'utilisateur
username_label = tk.Label(window, text='Nom d\'utilisateur :')
username_label.pack()
username_entry = tk.Entry(window, width=30)
username_entry.pack()

# Bouton pour créer le compte utilisateur
create_button = tk.Button(window, text='sauvegarde du compte utilisateur', command=sauvegarder_compte_utilisateur)
create_button.pack(pady=10)

window.mainloop()

#s.sendline('sudo passwd -e ' + str(nouvel_utilisateur)) # change mdp 1ière connection