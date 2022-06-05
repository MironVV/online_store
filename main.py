"""
ch: Переменная продолжения совершения покупок (значения y/n)
selectedCategory: переменная содержащая номер выбранной категории
cat_Name: переменная содержащая наименование выбранной категории
selectedProduct: переменная содержащая номер выбранного товара
"""
import re

from utils.password import check_buyer
from utils.category import Category
from utils.product import Product
from utils.basket import Basket

"""
Проверка логина и пароль пользователя
"""

check_buyer()

ch = 'y'

totalBasketList = {}  # словарь будет использоваться для подсчета количества и суммы товара в корзине
j = 1  # ключ словаря totalBasketList

while ch == 'y':

    """
    Вывод списка категории товара
    """
    Category.checkCategory()

    selectedCategory = int(input('Выбранная категория: '))

    """
    Проверка существования номера категории
    """
    while (selectedCategory not in [1, 2, 3, 4]):
        print('Выбранной категории не существует')
        selectedCategory = int(input('Выберите категорию: '))

    """
    Отображение наименований выбранной категории
    """
    cat_Name = Category(0, '')
    if selectedCategory == 1:
        cat_Name.set_category_name('Молочные продукты')
    elif selectedCategory == 2:
        cat_Name.set_category_name('Овощи и фрукты')
    elif selectedCategory == 3:
        cat_Name.set_category_name('Мясо и птица')
    elif selectedCategory == 4:
        cat_Name.set_category_name('Хлеб и выпечка')
    else:
        print('Указанной категории не существует')

    print(cat_Name.get_category_name())

    """
    Вывод списка товара из указанной категории
    """
    i = 1
    product_dic = {}  # создаем пустой словарь
    with open("list.txt", encoding="utf-8") as f:
        for line in f:
            if line.split(",")[0] == cat_Name.get_category_name():
                product_srt = Product(line.split(",")[1], line.split(",")[2], line.split(",")[3])
                product_dic[i] = product_srt.productName, product_srt.productPrice  # в цикле заполняем словарь названием товара
                print(i, 'Название товара: ', product_srt.productName)
                print(' ' * 4, 'Цена: ', product_srt.productPrice)
                print(' ' * 4, 'Рейтинг товара', product_srt.productRating)
                i += 1  # подсчет количества строк

    """
    Отображение добавленного в корзину товара
    """
    selectedProduct = int(input('Выбранный товар: '))

    """
    Проверка существования выбранного товара
    """
    while selectedProduct not in product_dic.keys():
        print('Указанного товара не существует. Выберите товар')
        selectedProduct = int(input('Выбранный товар: '))
    """
    Добавление выбранного товара в корзину
    """
    if selectedProduct in product_dic:
        basket1 = Basket(product_dic[selectedProduct])
        basket2 = re.sub("[(|'|)]", "", str(basket1.productName))
        print('В корзину добавлен товар: ', basket2)
        basket3 = int(basket2.rpartition(' ')[-1])
        totalBasketList[j] = basket3  # Запись данных о добавленном товаре

    ch = input('Продолжить покупки (y/n)? ').lower()  # выбор продолжения (завершения) покупки без учета регистра введенного символа
    j += 1
    """
    Вывод итоговых данных о количестве товара и сумме покупки
    """
    if ch == 'n':
        Basket.basketSum(totalBasketList)
