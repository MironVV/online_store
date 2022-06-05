"""
Модуль для работы с товарами в корзине
"""


class Basket:
    """
    Функция суммирования стоимости товара
    """

    def __init__(self, productName=None, productPrice=None):
        self.productName = productName  # Название товара
        self.productPrice = productPrice  # Цена товара

    def basketSum(self):
        b = list(self.values())
        print(f'В корзине  {len(self)} шт. товара на сумму: {sum(b)}')
