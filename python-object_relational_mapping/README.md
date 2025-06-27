# Python - Object-relational mapping

## Description

Ce projet est une démonstration de l’utilisation d’un ORM en Python pour interagir avec une base de données relationnelle sans écrire de SQL brut. À l’aide de SQLAlchemy, nous modélisons des entités Python qui sont automatiquement traduites en tables, colonnes, et relations SQL.

## Contenu du projet

- models.py – Définition des classes ORM (tables)

- database.py – Connexion et configuration de la base

- main.py – Script principal pour manipuler les données

- test_orm.py – Tests unitaires simples

- README.md – Documentation du projet

## Technologies utilisées

- Python 3.x

- SQLAlchemy

- SQLite (par défaut, peut être adapté à PostgreSQL, MySQL, etc.)

## Installation

```
git clone https://github.com/ton-utilisateur/ton-projet-orm.git
cd ton-projet-orm
python3 -m venv venv
source venv/bin/activate  # Windows : venv\Scripts\activate
pip install -r requirements.txt
python main.pyfrom sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Utilisateur(Base):
    __tablename__ = 'utilisateurs'
    id = Column(Integer, primary_key=True)
    nom = Column(String)
    email = Column(String, unique=True)
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Utilisateur(Base):
    __tablename__ = 'utilisateurs'
    id = Column(Integer, primary_key=True)
    nom = Column(String)
    email = Column(String, unique=True)

```
## Test

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Utilisateur(Base):
    __tablename__ = 'utilisateurs'
    id = Column(Integer, primary_key=True)
    nom = Column(String)
    email = Column(String, unique=True)

## Vérification du style de code avec pytest

def test_creation_utilisateur():
    user = Utilisateur(nom="Jean", email="jean@example.com")
    assert user.nom == "Jean"


## Toutes les informations

Ce README.md inclut nécessaires :

1. L'installation du projet avec les commandes "git clone", "cd" et l'exécution.
2. La structure du code Python recommandée.
3. Un exemple de code pour imprimer "Bonjour, le monde !".
4. La méthode pour vérifier le style de code avec "pycodestyle".

