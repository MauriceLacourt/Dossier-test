from tkinter import filedialog, messagebox
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

    # Extraire le texte visible de la balise body
    page_text = soup.prettify().strip()

    # Afficher le texte brut à l'écran
    print(page_text)

    # Demander à l'utilisateur où enregistrer le fichier
    fichier_enregistrement = filedialog.asksaveasfilename(title="Sélectionnez l'emplacement d'enregistrement", defaultextension=".txt")

    # Enregistrer le texte brut si l'utilisateur a choisi un emplacement
    if fichier_enregistrement:
        with open(fichier_enregistrement, "w", encoding="utf-8") as f:
            f.write(page_text)

        messagebox.showinfo("Enregistrement réussi", "Le texte brut a été enregistré dans le fichier '{}'.".format(fichier_enregistrement))
    else:
        print("Enregistrement annulé.")
else:
    print("Aucun fichier HTML sélectionné.")




