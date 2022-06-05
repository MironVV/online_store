"""
Модуль для работы с товарами
"""


class Product:
    def __init__(self, productName=str, productPrice=float, productRating=int):
        self.productName = productName  # Название товара
        self.productPrice = productPrice  # Цена товара
        self.productRating = productRating  # Рейтинг товара
