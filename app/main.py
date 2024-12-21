from fastapi import FastAPI
from .scraper import scrape_offers  # Importa a função de scraping do scraper.py

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Bem-vindo ao Chuvas de Ofertas!"}

@app.get("/scrape")
def get_offers():
    offers = scrape_offers()  # Chama a função de scraping
    return {"offers": offers}
