# LITRevu - Plateforme de Critiques Littéraires

![Logo](https://user.oc-static.com/upload/2023/06/29/168805567091_LITrevu%20banner.png)

## Introduction

LITRevu est une plateforme interactive dédiée aux critiques de livres et d'articles, construite avec le framework Django. Que vous soyez un passionné de littérature cherchant des recommandations ou un critique littéraire souhaitant partager vos opinions, LITRevu offre un espace centralisé pour explorer, demander et publier des critiques.

## Fonctionnalités Principales

### Billets

- **Création de Billets** : Les utilisateurs peuvent rédiger des billets pour demander des critiques sur des livres ou des articles.
- **Réponses aux Billets** : Les utilisateurs suivis peuvent poster des critiques en réponse aux billets d'autres utilisateurs.
- **Création Simultanée** : Possibilité de créer un billet et une critique pour ce billet en une seule étape.

### Flux

- **Affichage du Flux** : Le flux affiche les billets et critiques des utilisateurs suivis, y compris ceux de l'utilisateur connecté.
- **Ordre Antéchronologique** : Le flux est organisé par ordre antéchronologique, avec les actions les plus récentes en tête.

### Utilisateurs Suivis

- **Suivi d'Utilisateurs** : Les utilisateurs peuvent suivre d'autres utilisateurs pour voir leurs critiques.
- **Gestion des Abonnements** : Page listant les utilisateurs suivis avec une option pour cesser de suivre un utilisateur.

### Authentification

- **Inscription et Connexion** : Page d'inscription et de connexion pour les utilisateurs.

### Fonctionnalités Utilisateur Connecté

- **Gestion du Flux** : Consulter le flux, créer des billets, des critiques, et voir/modifier/supprimer ses propres billets et critiques.
- **Gestion des Abonnements** : Suivre, arrêter de suivre ou bloquer d'autres utilisateurs.

## Captures d'écran

## Captures d'écran

![Capture d'écran 1](https://image.noelshack.com/fichiers/2023/48/4/1701345590-opera-instantane-2023-11-30-125920-127-0-0-1.png)
![Capture d'écran 2](https://image.noelshack.com/fichiers/2023/48/4/1701345597-opera-instantane-2023-11-30-123140-127-0-0-1.png)

## Installation et Développement

1. **Cloner le Dépôt :**
   ```bash
   git clone https://github.com/ChangayaMusic/LITRevu.git

2. **Installer les Dépendances :**
   ```bash
   cd LITRevu
   pip install -r requirements.txt

3. **Appliquer les Migrations :**
   ```bash
   python manage.py migrate

4. **Lancer le Serveur de Développement :**
   ```bash
   python manage.py runserver
   Accédez à l'application à l'adresse http://localhost:8000.

## Spécifications Techniques

- **Framework:** Django
- **Base de Données :** SQLite (fichier db.sqlite3 inclus dans le repository)
- **Conformité PEP8 :** Respecter les directives de la PEP8

## Contribution

Nous accueillons les contributions ! 

## Auteurs

Fabien Lavieu

##Licence

Ce projet opensource
