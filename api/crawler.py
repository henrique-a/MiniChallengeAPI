import requests
from bs4 import BeautifulSoup

produto = input('Produto: ')
url = 'https://www.carrefour.com.br/busca?termo=' + produto
source_code = requests.get(url)
html_text = source_code.text
soup = BeautifulSoup(html_text, 'html.parser')

for price in soup.findAll('span', {'class': 'prd-price-new'}):
   print(price.text)
    