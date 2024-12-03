# Scrapy Project: GammVert Scraper

Ce projet Scrapy contient deux spiders destinés à scraper des données depuis le site **GammVert**. Il a été conçu pour explorer les catégories du site et collecter des informations détaillées sur les produits disponibles.

## Description des spiders

### 1. `gammvertspider`
- **Objectif** : Extraire les catégories principales et sous-catégories du site.
- **Fonctionnement** :
  - Accède à la page principale du site et identifie les catégories.
  - Parcourt les sous-catégories de manière récursive.
  - Exclut certaines catégories spécifiques (`Noël`, `Promotions`, `Conseils & idées`).
  - Stocke les informations des catégories dans un fichier JSON pour être utilisées par le deuxième spider.

- **Sortie** :
  - Pour chaque catégorie :
    - Nom de la catégorie
    - URL de la catégorie
    - Indicateur si la catégorie contient directement des produits (`is_page_list`).

### 2. `gammvert`
- **Objectif** : Scraper les produits à partir des catégories collectées par `gammvertspider`.
- **Fonctionnement** :
  - Lit un fichier JSON contenant les catégories (`data.json`).
  - Pour chaque catégorie avec des produits (`is_page_list = True`), récupère les détails des produits :
    - Nom
    - Note
    - Prix
    - ID du produit
    - Catégorie principale
    - Sous-catégorie principale
    - URL du produit
  - Navigue sur les pages suivantes si nécessaire.

- **Sortie** :
  - Informations détaillées des produits, exportées dans un fichier ou une base de données via le pipeline.

## Installation

1. Clonez le projet :
   ```bash
   git clone git@github.com:HerculePoivrot/Scraping_GammVert.git
