# 🐍 Python – Server-Side Rendering

Projet du programme **Holberton School – Higher Level Programming** axé sur le **rendu côté serveur** avec Python. L’objectif est de comprendre comment générer dynamiquement des pages HTML à partir du backend, en utilisant des templates et des données côté serveur.


## 🚀 Objectifs du projet

- Comprendre le concept de **Server-Side Rendering (SSR)**
- Utiliser **Flask** (ou Django) pour créer une application web
- Gérer les routes et les vues dynamiques
- Utiliser des **templates Jinja2** pour générer du HTML
- Passer des données Python aux templates
- Servir des fichiers statiques (CSS, images)
- Gérer les erreurs et les redirections

## 🧪 Fonctionnalités

- Page d’accueil dynamique
- Page utilisateur personnalisée (`/user/<name>`)
- Gestion des erreurs 404
- Utilisation de boucles et conditions dans les templates
- Intégration de styles CSS

## 🛠 Technologies utilisées

- Python 3.x
- Flask (micro-framework web)
- Jinja2 (moteur de templates)
- HTML5 / CSS3

## 📦 Installation

1. Clone le dépôt :
   ```bash
   git clone https://github.com/Plxii/holbertonschool-higher_level_programming.git

pip install -r requirements.txt

python app.py

## Exemple de route Flask

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', username=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'), 404

if __name__ == '__main__':
    app.run(debug=True)



