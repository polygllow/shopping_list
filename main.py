import shopping_data as sd
#Список покупок
items = []
prices = {}
bought = set()

#Бесконечный цикл, выход по команде 'exit'
while True:
    command = input('Введите команду: ').strip()
    #Выход из программы
    if command == 'exit':
        break
    #Вывести доступные команды
    elif command == 'help':
        print(sd.show_help())
    #Вывести случайный совет
    elif command == 'tip':
        print(sd.random_tip())
    #Добавление товара
    elif command.startswith('add '):
        product = command[4:].strip()
        if product not in items:
            items = sd.add_item(items, product)
        else:
            print('Товар уже есть в списке.')
    #Удаление товара
    elif command.startswith('remove '):
        product = command[7:].strip()
        if product in items:
            items = sd.remove_item(items, product)
        else:
            print('Такого товара нет в списке.')
    #Показывает текущий список
    elif command == 'list':
        print(sd.list_items(items))
    #Отчищает список
    elif command == "clear":
        items.clear()
        prices.clear()
        bought.clear()
        print('Список очищен.')
    #Добавляет товар в множество купленных товаров
    elif command.startswith('buy '):
        product = command[4:].strip()
        if product in items:
            print(f'Товары {sd.mark_bought(bought, product)} куплены.')
        else:
            print('Такого товара нет в списке.')
    #Выводит множество купленных товаров
    elif command == 'bought':
        print(f'Купленные товары: {bought}')
    #Добавляет значение в словарь prices
    elif command.startswith('price '):
        parts = command[6:].strip().split()
        product = parts[0]
        price_str = parts[1]
        if product in items:
            try:
                price = float(price_str)
                prices[product] = price
            except ValueError:
                print('Цена должна быть числом.')
        else:
            print('Такого товара нет в списке.')
    #Выводит сумму всех значений словаря prices
    elif command == 'total':
        print(sd.total(prices))
    #Выводит список товаров, которые стоят больше 100
    elif command == 'expensive':
        print(sd.expensive(items, prices))
    #Выводит названия из списка большими буквами
    elif command == 'upper':
        print([i.upper() for i in items])
    else:
        print('Такой команды нет.')