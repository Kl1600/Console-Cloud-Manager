import re
from password import hash_password
from api.auth_routes import save_user
import requests
import json
import base64

pattern_email=r'^[a-zA-Z0-9._]+@[a-z]{2,}.[a-z]{2,}$'
pattern_password=r'^[A-Z._-?!:;,1-9]+{5,15}$'

def create_user():
    email_user=None
    password_user=None
    password_hasher=None
    email_statut=False
    password_statut=False
    while email_statut==False:
         email_user=str(input("Entrez votre email :"))
         if re.match(pattern_email, email_user):
              print("Email valide")
              email_statut=True
         else:
             print("Email invalide")
             email_statut=False
    while password_statut==False:
         password_user=str(input("Entrez votre mot de passe :"))
         if re.match(pattern_password, password_user):
              print("Mot de passe valide")
              password_statut=True
              password_hasher=hash_password(password_user)
         else:
              print("Mot de passe invalide")
              password_statut=False
              password_hasher=None
    save_user(email_user, password_hasher)   
    return "Votre compte a été créé avec succès !"





