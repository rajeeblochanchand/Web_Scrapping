import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv

base_url = 'https://quotes.toscrape.com/'
page_count = 1

current_page_url = base_url

with open('quotes.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    fields = ['Quote', 'Author','Tags','Page']
    writer.writerow(fields)
    while(current_page_url):
        try:
            response = requests.get(current_page_url)
            soup = BeautifulSoup(response.text, 'lxml')
        except Exception as e:
            print(f'Error fetching page {page_count}: {e}')
            break
        else:
            quotes = soup.find_all('div', class_='quote')
            print(f'--- Page {page_count} ---')
            for quote in quotes:
                quote_text = quote.find('span', class_='text').text
                author_name = quote.find('small', class_='author').text
                tags = [tag.text for tag in quote.find_all('a', class_ = 'tag')]
                tags_string = ';'.join(tags)
                print(f'Quote: {quote_text}\nAuthor: {author_name}')
                writer.writerow([quote_text, author_name, tags_string, page_count])
                print('\n')

            next_button = soup.find('li', class_='next')
            if next_button:
                page_count += 1
                next_a = next_button.find('a')
                relative_url = next_a['href']
                next_page_url = urljoin(base_url, relative_url)
                current_page_url = next_page_url
            else:
                current_page_url = None


