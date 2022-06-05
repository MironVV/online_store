"""
Модуль для работы с категориями товара
"""


class Category:
    """
    Функция вывода списка категорий товара
    """

    def __init__(self, categoryNum=int, categoryName=None):
        self.__categoryNum = categoryNum  # Номер категории
        self.__categoryName = categoryName  # Название категории товара

    @staticmethod
    def checkCategory():
        print('Выберете категорию')
        with open('list.txt', encoding='utf-8-sig') as file:
            res_list = []

            for line in file:
                list_inp = line.split(",")[0]
                if list_inp not in res_list:
                    res_list.append(list_inp)
            i = 1
            for line in res_list:
                print(f'{i} - {line}')
                i += 1

    def set_category_name(self, categoryName):
        self.__categoryName = categoryName

    def get_category_name(self):
        return self.__categoryName
