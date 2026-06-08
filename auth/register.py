import re
from password import hash_password

pattern_email=r'^[a-zA-Z0-9._]+@[a-z]{2,}.[a-z]{2,}$'
pattern_password=r'^[A-Z._-?!:;,1-9]+{5,15}$'

email_user=None
password_user=None
email_statut=False
password_statut=False

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
    return email_user,password_user


password_hasher=hash_password(password_user)


import requests
import base64
import json
from auth.register import password_hasher,email_user


def save_user(email_user, password_hasher):

    TOKEN = ""
    OWNER = "Kl1600"
    REPO = "Console-Cloud-Manager"
    PATH = "compte.json"

    data = {
        "email_user": email_user,
        "password_user": password_hasher
    }

    contenu = json.dumps(data, indent=2)

    url = f"https://api.github.com/repos/{OWNER}/{REPO}/contents/{PATH}"

    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Accept": "application/vnd.github+json"
    }

    r = requests.get(url, headers=headers)

    sha = None

    if r.status_code == 200:
        sha = r.json()["sha"]

    payload = {
        "message": "Mise à jour des données",
        "content": base64.b64encode(
            contenu.encode("utf-8")
        ).decode("utf-8")
    }

    if sha:
        payload["sha"] = sha

    response = requests.put(
        url,
        headers=headers,
        json=payload
    )
     
    

              
    