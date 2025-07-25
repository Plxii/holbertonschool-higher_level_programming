# 🧠 Python – Everything Is Object

Ce projet explore la philosophie fondamentale de Python : **tout est un objet**. Que ce soit un entier, une chaîne de caractères, une fonction ou une classe, tout repose sur des instances d’objets. Ce module vise à comprendre les mécanismes d'identité, de mutabilité, d'affectation et de copie des objets en Python.


## 🚀 Objectifs du projet

- Comprendre que **toute valeur en Python est un objet**
- Analyser l’**identité**, le **type**, et la **valeur** des objets
- Différencier les objets **mutables** et **immuables**
- Explorer les effets d’affectation et de copie
- Découvrir les comportements inattendus liés à la mutabilité
- Utiliser des outils comme `id()`, `type()`, `is`, `==`

## 🧪 Concepts abordés

| Fichier                     | Concept clé                     |
|----------------------------|---------------------------------|
| `1-id.py`                  | Identité d’un objet             |
| `3-type_list.py`           | Types d’éléments dans une liste |
| `5-index_replace.py`       | Mutation d’une liste            |
| `6-list_copy.py`           | Différences entre copie et référence |
| `8-mutable.py`             | Mutabilité inattendue           |
| `9-copy_list.py`           | Fonction de copie sûre          |
| `100-magic_string.py`      | Fermeture avec état persistant |
| `101-locked_class.py`      | Classe restreinte avec `__slots__` |

## 🛠 Technologies utilisées

- Python 3.x

## 📚 Commandes utiles

- Vérifier l’identité :
  ```python
  id(my_var)
 --Test--
a is b   # Identité
a == b   # Égalité de valeur

