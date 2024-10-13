# Importer le module SnowballStemmer de NLTK
from nltk.stem.snowball import SnowballStemmer

# Créer un objet SnowballStemmer pour l'anglais
stemmer = SnowballStemmer("english")

# Liste de mots à tester
words = [
    "running",     # Cas de "ing"
    "jumps",       # Cas de "s"
    "easily",      # Cas de "ly"
    "national",    # Cas de "al"
    "happiness",   # Cas de "ness"
    "universe",    # Cas normal sans suffixe
    "relational",  # Cas de "ional"
    "rationally",  # Cas de "ally"
    "generalization", # Cas de "ization"
    "caresses",    # Cas de "sses"
    "flying",      # Cas de "ing"
    "studies",     # Cas de "ies"
    "tied",        # Cas de "ed"
    "hoped",       # Cas de "ed"
    "arguing",     # Cas de "ing"
    "unhappiness", # Préfixe "un" et suffixe "ness"
    "organization",# Cas de "ation"
    "committed",   # Doublage de consonne avant "ed"
    "hopping",     # Doublage de consonne avant "ing"
]

# Appliquer le stemming à chaque mot
stemmed_words = [stemmer.stem(word) for word in words]

# Afficher les résultats
print("Original Words:", words)
print("Stemmed Words:", stemmed_words)
