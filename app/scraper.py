import requests
from bs4 import BeautifulSoup

def scrape_offers():
    url = 'https://fratucci.com.br/site/promocao'  # Substitua com a URL real
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    offers = []
    # Exemplo de scraping (ajuste de acordo com a estrutura da página)
    for item in soup.find_all('div', class_='offer-item'):
        title = item.find('span', class_='title').text
        price = item.find('span', class_='price').text
        offers.append({"title": title, "price": price})

    return offers
