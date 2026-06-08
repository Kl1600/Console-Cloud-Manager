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
    if save_user(email_user,password_hasher)==200:
        return "Votre compté a été créé avec succès"
    else: 
        return "Erreur : veuillez recommencez"


import requests
import json
import base64


def save_user(email_user, password_hasher):

    TOKEN = ""
    OWNER = "Kl1600"
    REPO = "Console-Cloud-Manager"
    FICHIER = "compte.json"

    url = f"https://api.github.com/repos/{OWNER}/{REPO}/contents/{FICHIER}"

    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Accept": "application/vnd.github+json"
    }

    response = requests.get(url, headers=headers)

    users = []
    sha = None

    if response.status_code == 200:

        file_data = response.json()

        sha = file_data["sha"]

        content_base64 = file_data["content"]

        content = base64.b64decode(
            content_base64
        ).decode("utf-8")

        # Si le fichier n'est pas vide
        if content.strip():

            try:
                users = json.loads(content)

            except json.JSONDecodeError:
                print("Le fichier compte.json n'est pas un JSON valide.")
                return

        else:
            users = []

    elif response.status_code == 404:

        # Le fichier n'existe pas encore
        users = []

    else:

        print("Erreur GET :", response.status_code)
        print(response.text)
        return

    # Ajout du nouvel utilisateur
    users.append({
        "email_acc": email_user,
        "password_acc": password_hasher
    })

    # Conversion en JSON
    json_content = json.dumps(
        users,
        indent=4,
        ensure_ascii=False
    )

    # Encodage Base64 pour GitHub
    encoded_content = base64.b64encode(
        json_content.encode("utf-8")
    ).decode("utf-8")

    payload = {
        "message": f"Ajout utilisateur {email_user}",
        "content": encoded_content
    }

    # Obligatoire si le fichier existe déjà
    if sha is not None:
        payload["sha"] = sha

    response = requests.put(
        url,
        headers=headers,
        json=payload
    )

    print("Status :", response.status_code)
    print(response.text)

    return response.status_code


save_user(
    "promopro01700@gmail.com",
    "Motdepasse10"
)