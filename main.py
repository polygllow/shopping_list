import shopping_data as sd
#Список покупок
items = ""
#Бесконечный цикл, выход по команде 'exit'
while True:
    command = input("Введите команду: ").strip()
    #Выход из программы
    if command == "exit":
        break
    #Вывести доступные команды
    elif command == "help":
        print(sd.show_help())
    #Вывести случайный совет
    elif command == "tip":
        print(sd.random_tip())
    #Добавление товара
    elif command.startswith("add "):
        product = command[4:].strip()
        items = sd.add_item(items, product)
    #Удаление товара
    elif command.startswith("remove "):
        product = command[7:].strip()
        items = sd.remove_item(items, product)
    #Показывает текущий список
    elif command == "list":
        print(sd.list_items(items))
    #Отчищает список
    elif command == "clear":
        items = ""
        print("Список очищен.")

