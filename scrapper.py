import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

base_url = 'https://quotes.toscrape.com/'
response = requests.get(base_url)
#print(response.text)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('div', class_='quote')
for quote in quotes:
    quote_text = quote.find('span', class_='text').text
    author_name = quote.find('small', class_='author').text
    print(f'Quote: {quote_text}\nAuthor: {author_name}')
    print('\n')

next_button = soup.find('li', class_='next')
if next_button:
    next_a = next_button.find('a')
    relative_url = next_a['href']
    next_page_url = urljoin(base_url, relative_url)