import re
from password import hash_password

pattern_email=r'^[a-zA-Z0-9._]+@[a-z]{2,}.[a-z]{2,}$'
pattern_password=r'^[A-Z._-?!:;,1-9]+{5,15}$'

email_user=None
password_user=None
email_statut=False
password_statut=False
password_hasher_statut=False

def create_user():
    while email_statut!=True:
         email_user=str(input("Entrez votre email :"))
         if re.math(pattern_email, email_user):
              print("Email valide")
              email_statut=True
         else:
             print("Email invalide")
             email_statut=False
    while password_statut!=True:
         password_user=str(input("Entrez votre mot de passe :"))
         if re.match(pattern_password, password_user):
              print("Mot de passe valide")
              password_statut=True
         else:
              print("Mot de passe invalide")
              password_statut=False
    while password_hasher_statut!=True:
         password_hasher=hash_password(password_user)
         password_hasher_statut=True
    return "Votre compte a été créé avec succès !"


import requests
import json
import base64


def save_user(email_user, password_hasher):
     pass
