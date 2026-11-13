import random
TIPS = [
'Проверяйте сроки годности перед покупкой',
'Берите с собой список покупок',
'Покупайте овощи и фрукты по сезону'
]
random.seed(42)

def random_tip():
    return random.choice(TIPS)

def show_help():
    return '''
Доступные команды: 
add <товар> - добавить
remove <товар> - удалить
list - показать список
clear - отчистить список
tip - случайный совет
help - показать доступные команды
buy - купить товар
bought - список купленных товаров
price <товар> <цена> - ввести цену
total - общая стоимость
expensive - товары дороже 100
upper - список товаром большими буквами
exit - выход
'''

def list_items(items):
    if items:
        return items
    else:
        return 'Список пуст'

def add_item(items, name):
    items.append(name)
    print(f'Товар {name} добавлен.')
    return items

def remove_item(items, name):
    items.remove(name)
    print(f'Товар {name} удалён.')
    return items

def mark_bought(bought, name):
    bought.add(name)
    return bought

def expensive(items, prices):
    return [i for i in items if prices.get(i, 0) > 100]

def total(prices):
    total_price = 0
    for name, price in prices.items():
        total_price += price
    return total_price
