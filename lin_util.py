#! /usr/bin/python3
# -*- coding: utf-8 -*-

import paramiko
import sys
import tkinter as tk
from tkinter import scrolledtext

# Informations de connexion SSH
ssh_host = '10.0.2.14' # Adresse IP ou nom de domaine du serveur SSH
ssh_port = 22  # Port SSH
ssh_username = "ac"  # Nom d'utilisateur SSH
ssh_password = "Pza123RR"  # Mot de passe SSH

# Fenêtre Tkinter
window = tk.Tk()
window.title('Liste des comptes d\'utilisateur Linux')
window.geometry('500x400')

# Zone de texte pour afficher les résultats
results_text = scrolledtext.ScrolledText(window, width=60, height=15)
results_text.pack(pady=10)

#  Exécution de la commande pour extraire les comptes d'utilisateur
commande_shell = "awk -F':' '{ if ($3 >= 1000 && $3 != 65534) print $1 }' /etc/passwd"

# Fonction pour lister les comptes d'utilisateur via SSH
def lister_comptes_utilisateur():
    # Création d'une instance de client SSH
    client_ssh = paramiko.SSHClient()
    client_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Connexion au serveur SSH
        client_ssh.connect(ssh_host, ssh_port, ssh_username, ssh_password)

        # Exécution de la commande
        stdin, stdout, stderr = client_ssh.exec_command(commande_shell)

        # Affichage des résultats de la commande
        print("Résultats de la commande :")
        print(stdout.read().decode("utf-8"))

    except paramiko.AuthenticationException:
        print("Échec de l'authentification SSH.")
    except paramiko.SSHException as e:
        print("Erreur lors de la connexion ou de l'exécution de la commande SSH:", str(e))
    finally:
        client_ssh.close()
        quit()

# Bouton pour lister le comptes utilisateurs
create_button = tk.Button(window, text='lister les comptes utilisateurs', command=lister_comptes_utilisateur)
create_button.pack(pady=10)

#executer_commande_ssh(commande_shell)

window.mainloop()
