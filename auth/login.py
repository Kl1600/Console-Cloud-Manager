from api.auth_routes import recup_contenu
from password import hash_password

def login_user():
    email=str(input("Entrez votre email :"))
    password=str(input("Entrez votre mot de passe :"))
    indice=-1
    contenu=recup_contenu()
    if email not in contenu:
        print("vous n'avez pas de compte")
    else:
        for i in contenu:
            indice=indice+1
            if contenu([indice]['email'])==email:
                password_hasher=hash_password(password)
                if contenu([indice]['mdp'])==password_hasher:
                    print("Connexion avec succès !!")
                    load_user()
        


def verify_password(password):
    contenu=recup_contenu()
    if password in contenu:
        pass
        

def load_user():
    pass
    
