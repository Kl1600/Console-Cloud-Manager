# Console-Cloud-Manager

Application Python en ligne de commande permettant la gestion d'utilisateurs, le stockage d'images sur Cloudinary, la gestion de données dans GitHub et l'exposition de ces ressources via une API REST FastAPI.

---

## 🚀 Fonctionnalités

### Authentification

* Création de compte
* Connexion utilisateur
* Vérification des identifiants
* Hashage sécurisé des mots de passe
* Gestion des sessions

### Gestion GitHub

* Connexion via Personal Access Token
* Lecture des repositories
* Création de fichiers
* Modification de fichiers
* Suppression de fichiers
* Consultation de l'arborescence d'un dépôt

### Gestion des données

* Stockage de données JSON dans GitHub
* Création
* Lecture
* Mise à jour
* Suppression
* Recherche

### Gestion des images

* Upload d'images vers Cloudinary
* Suppression d'images
* Consultation des URLs publiques
* Liste des médias hébergés

### API REST

* Authentification
* Gestion des données
* Gestion des images
* Documentation Swagger automatique

### Interface Console

* Menus interactifs
* Navigation simplifiée
* Validation des entrées utilisateur
* Gestion centralisée des erreurs

---

## 🏗️ Architecture

Le projet suit une architecture fonctionnelle stricte.

* Aucune Programmation Orientée Objet (POO)
* Une responsabilité par fonction
* Une fonction principale = un fichier de test dédié
* Modules indépendants
* Couplage faible
* Forte testabilité

```text
project/
│
├── main.py
│
├── config/
│   └── settings.py
│
├── auth/
│   ├── register.py
│   ├── login.py
│   ├── password.py
│   └── storage.py
│
├── github/
│   ├── repository.py
│   ├── files.py
│   └── api.py
│
├── cloudinary/
│   ├── upload.py
│   ├── delete.py
│   └── listing.py
│
├── data/
│   ├── create.py
│   ├── read.py
│   ├── update.py
│   ├── delete.py
│   └── search.py
│
├── api/
│   ├── app.py
│   ├── auth_routes.py
│   ├── data_routes.py
│   └── image_routes.py
│
├── cli/
│   ├── menu.py
│   ├── auth_menu.py
│   ├── github_menu.py
│   └── image_menu.py
│
├── tests/
│
├── requirements.txt
│
└── README.md
```

---

## 📦 Technologies

### Langage

* Python 3.12+

### API

* FastAPI
* Uvicorn
* Pydantic

### GitHub

* Requests
* PyGithub

### Cloudinary

* cloudinary

### Tests

* pytest
* pytest-mock
* coverage

---

## ⚙️ Installation

### Cloner le dépôt

```bash
git clone https://github.com/votre-utilisateur/console-cloud-manager.git

cd console-cloud-manager
```

### Créer un environnement virtuel

```bash
python -m venv .venv
```

### Activation

Linux / Mac :

```bash
source .venv/bin/activate
```

Windows :

```bash
.venv\Scripts\activate
```

### Installation des dépendances

```bash
pip install -r requirements.txt
```

---

## 🔐 Configuration

Créer un fichier `.env` à la racine du projet :

```env
GITHUB_TOKEN=

GITHUB_OWNER=

GITHUB_REPOSITORY=

CLOUDINARY_CLOUD_NAME=

CLOUDINARY_API_KEY=

CLOUDINARY_API_SECRET=
```

---

## ▶️ Lancement de l'application

### Interface Console

```bash
python main.py
```

### API REST

```bash
uvicorn api.app:app --reload
```

Documentation :

```text
http://localhost:8000/docs
```

```text
http://localhost:8000/redoc
```

---

## 🖥️ Utilisation

### Menu principal

```text
1. Connexion
2. Créer un compte
3. Quitter
```

### Menu utilisateur

```text
1. Voir mes données
2. Ajouter une donnée
3. Modifier une donnée
4. Supprimer une donnée
5. Upload image
6. Voir images
7. Gestion GitHub
8. Lancer API
9. Déconnexion
```

---

## 📚 API REST

### Authentification

| Méthode | Endpoint  |
| ------- | --------- |
| POST    | /register |
| POST    | /login    |

### Données

| Méthode | Endpoint   |
| ------- | ---------- |
| GET     | /data      |
| GET     | /data/{id} |
| POST    | /data      |
| PUT     | /data/{id} |
| DELETE  | /data/{id} |

### Images

| Méthode | Endpoint            |
| ------- | ------------------- |
| POST    | /images             |
| GET     | /images             |
| DELETE  | /images/{public_id} |

---

## 🧪 Tests

Chaque fonction métier possède :

* un fichier de test dédié ;
* un cas nominal ;
* un cas d'erreur ;
* un cas limite.

### Exécuter les tests

```bash
pytest
```

### Mode détaillé

```bash
pytest -v
```

### Couverture

```bash
coverage run -m pytest

coverage report

coverage html
```

Objectifs :

* 100 % des fonctions métier testées
* 90 % de couverture minimum
* Mocks obligatoires pour GitHub et Cloudinary

---

## 📊 Qualité du projet

### Standards

* Typage Python
* Docstrings
* Validation des entrées
* Logging centralisé
* Gestion des erreurs

### Architecture

* Fonctionnelle uniquement
* Pas de classes métier
* Pas de POO
* Découpage modulaire

---

## 🔒 Sécurité

* Hashage des mots de passe
* Variables d'environnement
* Validation des données utilisateur
* Gestion des exceptions
* Journalisation des actions sensibles

---

## 📈 Roadmap

### Version 2

* Authentification JWT
* Gestion des rôles
* Permissions avancées
* Interface Web
* Docker
* Déploiement cloud
* Gestion multi-repositories
* Tableau de bord d'administration

---

## 📄 Licence

MIT License

---

## 👨‍💻 Auteur

Projet réalisé dans le cadre d'un exercice d'architecture Python fonctionnelle combinant GitHub comme stockage distant, Cloudinary comme CDN média et FastAPI comme couche d'exposition REST.
