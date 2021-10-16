import requests
from bs4 import BeautifulSoup

# URL for web scraping
url = "https://dariusforoux.com/motivational-quotes/"

# Perform GET request
response = requests.get(url)
htmlContent = response.content 

# Parse HTML from the response
soup = BeautifulSoup(htmlContent,"html.parser")

#Extract quotes and authors html elements
all_quotes = soup.find_all('em')
all_authors = soup.find_all('strong')

#Extract quotes into a list
quotes=list()
for quote in all_quotes:
    quotes.append(quote.text)

#Extract authors into a list    
authors=list()
for author in all_authors:
    authors.append(author.text)

# Make a quote / author tuple for printing    
for t in zip(quotes, authors):
    print(t) 

