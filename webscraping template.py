import requests
from bs4 import BeautifulSoup

postLoginUrl = ''
scrapingUrl = ''


payload = {
    'username': input('Email:  '),
    'password': input('Password:  ')
}

# sessions are used to log into sites
with requests.Session() as session:
    # this sends the payload to log in
    post = session.post(postLoginUrl, data=payload)

    page = session.get(scrapingUrl)
    soup = BeautifulSoup(page.content, 'html.parser')


