from app import models

def add_price(name, value):
    models.update_price(name, value)

def get_all_prices():
    return models.get_prices()
