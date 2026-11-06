import random

def random_tip():
    number = random.randint(1,3)
    if number == 1:
        return 'Проверяйте сроки годности перед покупкой'
    elif number == 2:
        return 'Берите с собой список покупок'
    else:
        return 'Покупайте овощи и фрукты по сезону'

def show_help():
    return '''
Доступные команды: 
add <товар> - добавить
remove <товар> - удалить
list - показать список
clear - отчистить список
tip - случайный совет
help - показать доступные команды
exit - выход
'''

def list_items(items):
    if items:
        return items
    else:
        return 'Список пуст'

def add_item(items, name):
    if name == " ":
        print("Укажите название товара.")
    elif name not in items.split(", "):
        if items:
            items += ", " + name
            print(f"Товар {name} добавлен.")
        else:
            items = name
            print(f"Товар {name} добавлен.")
    else:
        print("Такой товар уже есть.")
    return items

def remove_item(items,name):
    if name not in items.split(", "):
        print("Такого товара нет в списке.")
    elif items == name:
        items = ""
        print(f"Товар {name} удален.")
    elif items.startswith(name + ", "):
        items = items.replace(name + ", ", "", 1)
        print(f"Товар {name} удален.")
    else:
        items = items.replace(", " + name, "", 1)
        print(f"Товар {name} удален.")
    return items
