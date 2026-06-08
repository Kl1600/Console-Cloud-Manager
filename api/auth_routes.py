import requests
import json
import base64

#enregistrement de nouveau compte dans compte.json
def save_user(email_user, password_hasher):
    TOKEN=""
    OWNER="Kl1600"
    REPO="Console-Cloud-Manager"
    FILE="compte.json"
    users={
         "email":email_user,
         "mdp":password_hasher
    }
    url=f"https://api.github.com/repos/{OWNER}/{REPO}/contents/{FILE}"
    headers={
         "authorization":f"bearer {TOKEN}"
    }
    reponse=requests.get(url, headers=headers)
    data_reponse=reponse.json()
    if reponse.status_code==200:
        contenu=data_reponse['content']
        contenubase64=base64.b64decode(contenu).decode("utf-8")
        contenu=json.loads(contenubase64)
        contenu.append(users)
    else:
         return "Erreur"
    sha=data_reponse['sha']
    texte_json=json.dumps(contenu)
    contenubase64=base64.b64encode(
        texte_json.encode("utf-8")
    ).decode("utf-8")
    payload={
         "message":"Compte enregistrer",
         "content":contenubase64,
         "sha":sha
    }
    requests.put(url, json=payload)
    return reponse.status_code

def recup_contenu():
    TOKEN=""
    OWNER="Kl1600"
    REPO="Console-Cloud-Manager"
    FILE="compte.json"
    url=f"https://api.github.com/repos/{OWNER}/{REPO}/contents/{FILE}"
    headers={
         "authorization":f"bearer {TOKEN}"
    }
    reponse=requests.get(url, headers=headers)
    data_reponse=reponse.json()
    if reponse.status_code==200:
        contenu=data_reponse['content']
        contenubase64=base64.b64decode(contenu).decode("utf-8")
        contenu=json.loads(contenubase64)
    else:
         return "Erreur"
    return contenu
    