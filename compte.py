from tkinter import filedialog
from bs4 import BeautifulSoup
import string
import re

# Ouvrir une boîte de dialogue de sélection de fichier
fichier_html = filedialog.askopenfilename(title="Sélectionnez votre fichier HTML")

# Vérifier si un fichier a été sélectionné
if fichier_html:

    # Détecter l'encodage du fichier HTML
    try:
        with open(fichier_html, "rb") as f:
            first_line = f.readline().decode("utf-8")
            encoding_match = re.search(r'charset[\s]*=[\s]*"([^"]*)"', first_line)
            if encoding_match:
                encoding = encoding_match.group(1).lower()  # Convertir l'encodage en minuscules
            else:
                encoding = "utf-8"  # Définir UTF-8 par défaut si introuvable
    except UnicodeDecodeError:
        encoding = "utf-8"  # Revenir à UTF-8 en cas d'erreur

    # Ouvrir le fichier HTML avec l'encodage détecté (ou par défaut)
    with open(fichier_html, "r", encoding=encoding) as f:
        html_content = f.read()

    # Créer un objet BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")

    # Extraire le texte de la page
    page_text = soup.get_text()

    # Diviser le texte en mots
    mots = page_text.split()

    # Définir une liste de mots vides
    mots_vides = set(string.punctuation + " ")

    # Filtrer les mots vides
    mots_filtres = [mot for mot in mots if mot not in mots_vides]

    # Afficher les mots filtrés
    for mot in mots_filtres:
        print(mot)
else:
    print("Aucun fichier sélectionné.")
