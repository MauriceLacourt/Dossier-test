import requests
from bs4 import BeautifulSoup
import re

def extract_emails(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    emails = []
    for email in soup.find_all("a", href=re.compile(r"^mailto:")):
        emails.append(email["href"].replace("mailto:", ""))

    return emails


if __name__ == "__main__":
    url = "https://www.example.com/"
    emails = extract_emails(url)
    print(emails)
