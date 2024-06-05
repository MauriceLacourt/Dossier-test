import requests
from bs4 import BeautifulSoup
import re

def extract_emails(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    emails = []

    for element in soup.find_all(name='a'):
        text = element.text
        match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', text)
        if match:
            emails.append(match.group())

    return emails


if __name__ == '__main__':
    url = input('Veuillez entrer l\'adresse du site : ')
    url = 'https://www.' + url
    emails = extract_emails(url)
    print(emails)

