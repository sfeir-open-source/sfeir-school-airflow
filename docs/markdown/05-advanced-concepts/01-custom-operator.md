# Problématique

Maintenant vous devez charger de la donnée dans une base Postgres.
Mais à partir d'un fichier CSV.

Problème : Il n'existe pas d'opérateur CSV vers Postgres

Solution : Créer notre propre opérateur

# Custom Operator

Il est possible de créer un opérateur custom pour répondre à un besoin particulier.

Deux pratiques :
- Surcharger un opérateur déjà existant
- Créer son propre opérateur from scratch

Dans notre cas, nous allons surcharger un opérateur existant

# LAB: Custom Operator

