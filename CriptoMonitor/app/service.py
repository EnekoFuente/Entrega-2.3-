from app import modelDB

def add_price(name, value):
    modelDB.update_price(name, value)

def get_all_prices():
    return modelDB.get_prices()
