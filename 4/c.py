"""
Зависимость
"""

class Product:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price
        

class Order:
    def __init__(self, *products) -> None:
        self.products = list(products)
    
    def calculate_total(self):
        total = 0        
        for product in self.products:
            total += product.price
        return total


class PaymentProcessor:
    def process_payment(self, order: Order):
        total_price = order.calculate_total()
        """
        Процесс оплаты продуктов
        """
        print(total_price, "- success!")
        return True


pr1 = Product('Book', 3000)
pr2 = Product('Ball', 6000)
order = Order(pr1, pr2)


paymentProcessor = PaymentProcessor()
paymentProcessor.process_payment(order)