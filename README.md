# Algorithmes de Stemming avec Snowball Stemmer et Porter Stemmer

Ce dépôt contient deux implémentations d'algorithmes de stemming : le Snowball Stemmer (via NLTK) et le Porter Stemmer. Le stemming est un processus de réduction des mots à leur forme racine ou base, utile dans les tâches de traitement du langage naturel (NLP).

## Fichiers

- **stemming.py** : Utilise le Snowball Stemmer de NLTK pour effectuer du stemming sur des mots en anglais.
- **porter_stemmer.sn** : Implémentation de l'algorithme Porter Stemmer en pseudo-code avec une série de règles pour retirer les suffixes des mots.

## Exemple de Stemming avec Snowball Stemmer (NLTK)

Dans le fichier `stemming.py`, nous utilisons le module `SnowballStemmer` de la bibliothèque NLTK pour appliquer du stemming sur une liste de mots anglais. Le Snowball Stemmer est une version améliorée du Porter Stemmer, permettant une meilleure gestion des langues.

### Utilisation

1. Installez la bibliothèque nécessaire :
   ```bash
   pip install nltk
