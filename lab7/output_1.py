class Product:
    def __init__(self, product_id, name, category, price):
        self.__product_id = product_id  # Приватне поле
        self.__name = name  # Приватне поле
        self.__category = category  # Приватне поле
        self.__price = price  # Приватне поле

    # Геттери
    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_category(self):
        return self.__category

    def get_price(self):
        return self.__price

    # Сеттери
    def set_name(self, name):
        self.__name = name

    def set_category(self, category):
        self.__category = category

    def set_price(self, price):
        if price >= 0:  # Додана валідація для ціни
            self.__price = price
        else:
            raise ValueError("Price cannot be negative")

class InventoryManagement:
    def __init__(self, products=None):
        if products is None:
            self.__products = []
        else:
            self.__products = products

    def add_product(self, product):
        self.__products.append(product)

    def remove_product(self, product_id):
        self.__products = [product for product in self.__products if product.get_product_id() != product_id]

    def print_product_details(self, product_id):
        for product in self.__products:
            if product.get_product_id() == product_id:
                print(f"Product ID: {product.get_product_id()}, Name: {product.get_name()}, Category: {product.get_category()}, Price: {product.get_price()}")

    def get_all_products(self):
        return self.__products

# Приклад використання
if __name__ == "__main__":
    # Створюємо декілька продуктів
    p1 = Product(1, "Laptop", "Electronics", 1200)
    p2 = Product(2, "Smartphone", "Electronics", 800)
    p3 = Product(3, "Book", "Stationery", 20)

    # Створюємо менеджер інвентаря та додаємо продукти
    inventory = InventoryManagement()
    inventory.add_product(p1)
    inventory.add_product(p2)
    inventory.add_product(p3)

    # Друкуємо деталі продукту з id 2
    inventory.print_product_details(2)
