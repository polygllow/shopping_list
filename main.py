#Список покупок
items = ""
#Бесконечный цикл, выход по команде 'exit'
while True:
    print("Команды: add-добавить, remove-удалить, list-показать список, clear-отчистить список, exit-выход")
    command = input("Введите команду: ").strip()
    #Выход из программы
    if command == "exit":
        break
    #Добавление товара
    elif command.startswith("add "):
        product = command[4:].strip()
        if product == "":
            print("Укажите название товара.")
        elif product not in items.split(", "):
            if items:
                items += ", " + product
            else:
                items = product
            print(f"Товар {product} добавлен.")
        else:
            print("Такой товар уже есть.")
    #Удаление товара
    elif command.startswith("remove "):
        product = command[7:].strip()
        if product not in items.split(", "):
            print("Такого товара нет в списке.")
        elif items == product:
            items = ""
            print(f"Товар {product} удален.")
        elif items.startswith(product + ", "):
            items = items.replace(product + ", ", "", 1)
            print(f"Товар {product} удален.")
        else:
            items = items.replace(", " + product, "", 1)
            print(f"Товар {product} удален.")
    #Показывает текущий список
    elif command == "list":
        print(items)
    #Отчищает список
    elif command == "clear":
        items = ""
        print("Список очищен.")

