import requests
from bs4 import BeautifulSoup

postLoginUrl = 'https://oyoclass.com/signin'

pageNum = 1
scrapingUrl = 'https://bmsteam.oyoclass.com/badges/all?page='

payload = {
    'username': input('Email:  '),
    'password': input('Password:  ')
}

# sessions are used to log into sites
with requests.Session() as session:
    # this sends the payload to log in
    post = session.post(postLoginUrl, data=payload)

    # <class 'bs4.element.ResultSet'> ~ This is a custom RuleSet
    while pageNum <= 24:
        page = session.get(scrapingUrl + str(pageNum))
        soup = BeautifulSoup(page.content, 'html.parser')

        for i in soup.findAll('p', {'class': 'cat_badge_name'}):
            print(i.get_text())  # the .get_text() removes the tags

        pageNum += 1


