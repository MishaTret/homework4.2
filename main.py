class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_quantity(self):
        return self.quantity


class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def sell_product(self, product_name, quantity):
        for product in self.products:
            if product.get_name() == product_name:
                if product.get_quantity() >= quantity:
                    product.quantity -= quantity
                    print(f"Sold {quantity} {product_name}(s)")
                    return
                else:
                    print("Not enough products in stock")
                    return
        print("Product not found")

    def get_total_revenue(self):
        total_revenue = 0
        for product in self.products:
            total_revenue += product.get_price() * product.get_quantity()
        return total_revenue


store = Store("My Store", "123")




