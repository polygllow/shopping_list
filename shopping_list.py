items = ""
while True:
    command = input("Введите команду: ").strip()
    if command == "exit":
        break
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
    elif command == "list":
        print(items)
    elif command == "clear":
        items = ""
        print("Список очищен.")

