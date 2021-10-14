import requests
from bs4 import BeautifulSoup

url = "https://dariusforoux.com/motivational-quotes/"

r = requests.get(url)
htmlContent = r.content 

soup = BeautifulSoup(htmlContent,"html.parser")

all_quotes = soup.find_all('em')
all_authors = soup.find_all('strong')

quotes=list()
for quote in all_quotes:
    quotes.append(quote.text)

authors=list()
for author in all_authors:
    authors.append(author.text)

for t in zip(quotes, authors):
    print(t) 

