# SQL - Introduction

## Description

Ce projet est une initiation pratique au langage SQL. Il a pour but de familiariser l’utilisateur avec la création de bases de données relationnelles, l’insertion de données et la réalisation de requêtes simples à complexes. Il s’adresse aux débutants souhaitant se familiariser avec les principes fondamentaux de la manipulation des données.

## Contenu du projet

- schema.sql : crée la structure de la base (tables, types, relations)

- data.sql : insère des données d'exemple dans la base

- queries.sql : contient différentes requêtes permettant de tester la base et d’explorer les données

- tests/test_queries.py : script de tests automatisés pour vérifier les résultats des requêtes (facultatif mais utile)

- README.md : documentation du projet

## Installation

```
Clone the repository and compile the code with "python3":

$ git clone https://github.com/Plxii/holbertonschool-higher_level_programming.git
$ cd holbertonschool-higher_level_programming
$ wc -m <nom-du-fichier>
$ ./holbertonschool-higher_level_programming
```
## Test

#!/usr/bin/python3

import sqlite3

def test_connection():
    conn = sqlite3.connect('base_de_donnees.db')
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM utilisateurs;")
    result = cur.fetchone()
    assert result[0] > 0, "La table utilisateurs doit contenir au moins une entrée."
    conn.close()

if __name__ == "__main__":
    test_connection()
    print("✅ Test passé avec succès.")

## Vérification du style de code avec pycodestyle

$ pip install pycodestyle
$ pycodestyle nom_du_fichier.py

## Toutes les informations

Ce README.md inclut nécessaires :

1. L'installation du projet avec les commandes "git clone", "cd" et l'exécution.
2. La structure du code Python recommandée.
3. Un exemple de code pour imprimer "Bonjour, le monde !".
4. La méthode pour vérifier le style de code avec "pycodestyle".
