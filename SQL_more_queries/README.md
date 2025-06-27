# SQL - Introduction

## Description

Ce projet approfondit l’apprentissage de SQL à travers l’écriture de requêtes plus avancées, portant sur l’analyse, la jointure multiple, les sous-requêtes, les vues et les fonctions d’agrégation. L’objectif est de renforcer ta compréhension des bases de données relationnelles en manipulant des données réelles ou simulées.

## Contenu du projet

schema.sql – Structure de la base de données (tables, types, clés)

data.sql – Jeu de données pour tester les requêtes

more_queries.sql – Requêtes complexes (jointures, agrégations, sous-requêtes, vues)

README.md – Présentation du projet

tests/test_queries.py – (Facultatif) Script Python pour automatiser des vérifications de résultats

## Objectifs

Écrire des requêtes SQL avancées avec jointures multiples

Manipuler des fonctions d’agrégation et des regroupements

Créer et interroger des vues

Utiliser des sous-requêtes dans les clauses SELECT, WHERE, ou FROM

Valider les résultats des requêtes à l’aide de tests simples

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

if __name__ == "__main__":
    import sqlite3

    def test_total_commandes():
        conn = sqlite3.connect("bdd.db")
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM commandes;")
        result = cur.fetchone()
        assert result[0] > 0, "❌ La table commandes devrait contenir au moins une ligne."
        conn.close()
        print("✅ Requête testée avec succès.")

    test_total_commandes()

## Toutes les informations

Ce README.md inclut nécessaires :

1. L'installation du projet avec les commandes "git clone", "cd" et l'exécution.
2. La structure du code Python recommandée.
3. Un exemple de code pour imprimer "Bonjour, le monde !".
4. La méthode pour vérifier le style de code avec "pycodestyle".

