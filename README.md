# Application Django de gestion des produits

Cette application minimaliste permet d'ajouter un produit dans une base de données SQLite via une interface Web.

## Prérequis

- Python 3.11 ou plus récent
- Un environnement virtuel Python est recommandé

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Utilisation

Appliquez les migrations et démarrez le serveur de développement :

```bash
python manage.py migrate
python manage.py runserver
```

Ensuite, rendez-vous sur [http://localhost:8000](http://localhost:8000) pour ajouter des produits.

## Tests

```bash
python manage.py test
```
