

class ProductInfo:
    def __init__(self, name, price, type):
        self.name = name
        self.price = price
        self.type = type

    def display_product(self):
        print(f"Name: {self.name}, Price: {self.price}, Type: {self.type}")


class ProductSearch:
    def __init__(self, products):
        self.products = products

    def search_product(self, query):
        result = [product for product in self.products if query.lower() in product.name.lower()]
        return result


class ProductOrder:
    def __init__(self, product):
        self.product = product

    def order_product(self, quantity):
        print(f"Ordered {quantity} of {self.product.name}")


if __name__ == "__main__":

    product1 = ProductInfo("Laptop", 1000, "Electronics")
    product2 = ProductInfo("Smartphone", 500, "Electronics")

    search = ProductSearch([product1, product2])
    search_results = search.search_product("Laptop")
    for product in search_results:
        product.display_product()


    order = ProductOrder(product1)
    order.order_product(3)
