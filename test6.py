import requests
from bs4 import BeautifulSoup
import re

def extract_emails(url):
    emails = []

    # Récupère la liste de toutes les pages du site
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    urls = [a['href'] for a in soup.find_all(name='a')]

    # Itère sur toutes les pages
    for u in urls:
        response = requests.get(u)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Recherche les adresses e-mail sur la page
        for element in soup.find_all(name='a'):
            text = element.text
            match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', text)
            if match:
                emails.append(match.group())

    return emails


if __name__ == '__main__':
    url = input('Veuillez entrer l\'adresse du site : ')
    emails = extract_emails(url)
    print(emails)

