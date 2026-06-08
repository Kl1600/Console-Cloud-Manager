from api.auth_routes import recup_contenu

def login_user():
    email=str(input("Entrez votre email :"))
    password=str(input("Entrez votre mot de passe :"))
    contenu=recup_contenu()
    if email not in contenu:
        print("vous n'avez pas de compte")
    else:
        verify_password(password)
        if verify_password(password)==True:
            print ("connection avec succès !")
        


def verify_password(password):
    pass

def load_user():
    pass
