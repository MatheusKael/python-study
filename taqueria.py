menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def main():

    total = []
    while True:
        try:
            item = input("item: ").strip().title()
        except EOFError:
            break

        if item in menu:

            total.append(menu[item])

            print(f"Total: ${sum(total)}")
        else:
            print("Item is not on the menu")


main()
