from mimetypes import init
pip install psycopg2
import psycopg2



class menuItems:
    def __init__(self, name:str,price:int):
        self.name = name
        self.price = price